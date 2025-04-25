import math
import re
import subprocess
import numpy as np
import time


## symbolic link from $OBSHOME/COMMON/task/pfsmisc.py to this file
def adc_pos(el,cnf):

    e={"WAVE1":[-0.0351, 11.7567, -0.8698,  0.7315, -0.1987],
       "WAVE2":[ 0.0222, 13.8148,  0.8844, -0.7712,  0.2237],
       "WAVE3":[ 0.0228,  4.8088,  1.8683, -0.5799, -0.2170],
       "WAVE4":[-0.0503, 12.6760, -0.8870,  0.7120, -0.1907],
       "WAVE5":[-0.0136, 15.9061, -0.1916,  0.2097, -0.0386],
       "WAVE9":[ 0.0027, 12.6755, -0.0992,  0.2141, -0.0901]}

    za=(90-el)*math.pi/180.

    t=math.tan(za)

    if cnf in e:
        pos=e[cnf][0] + e[cnf][1]*t + e[cnf][2]*math.pow(t,2) + e[cnf][3]*math.pow(t,3) +e[cnf][4]*math.pow(t,4)
        if pos < 0.:
            pos=0.
        elif pos > 22.:
            pos=22.
    else:
        pos=-99.

    # formating
    pos2="{0:.2f}".format(pos)

    #return pos
    return pos2

## lower case of characters

def lower(s) :

    return s.lower()

def gen2_round(f, n) :

    return round(f, n)


def random_song(music1,music2,music3,music4,music5):
    import random
    song = [music1,music2,music3,music4,music5]    
    return random.choice(song)

def sps_chk_sel(select, val) :

    if select == "cam" :
        if re.fullmatch(r'[brn]{1}[1-4]{1}(,[brn]{1}[1-4]{1})*', val) != None :
            ret = 1
        else :
            ret = 0

    elif select == "specNum" :
        if re.fullmatch(r'[1-4]{1}(,[1-4]{1})*', val) :
            ret = 1
        else :
            ret = 0
    elif select == "arm" :
        if re.fullmatch(r'[brmn]{1}(,[brn]{1})*', val) :
            ret = 1
        else :
            ret = 0

    else :

        ret = 0

    return ret

"""
def fullmatch(regex, string, flags=0):
    ###Emulate python-3.4 re.fullmatch().###
    return re.match("(?:" + regex + r")\Z", string, flags=flags)
"""


def inr_med10err(threshold):

    lastExpid  = None
    linenum    = 0
    c          = 0
    ln         = np.empty([0])
    thres_min  = threshold * -1
    thres_max  = threshold

    while True:

        # Check loop flag status

        l_raw = subprocess.check_output(['get_status', 'MEMORY.PFS'])
        l_lines = l_raw.decode('latin-1').split('\n')

        dl = {}
        for ll in l_lines:
            if not ll:
                continue
            lname, lval = ll.split(':')
            lname = lname.strip()         # delete extra space
            lname = lname.split('.')[-1]  # extract last content
            lval = lval.strip()

            if lname == 'ROTCORLOOP_FLG':
                dl[lname] = int(lval)
        
        if dl['ROTCORLOOP_FLG'] == 0:
            c = 0
            return c


        g_raw = subprocess.check_output(['get_status', 'STATL.GU'])
        g_lines = g_raw.decode('latin-1').split('\n')

        dg = {}
        for lg in g_lines:
            if not lg:
                continue
            gname, gval = lg.split(':')
            gname = gname.strip()         # delete extra space
            gname = gname.split('.')[-1]  # extract last content
            gval = gval.strip()

            if gname == 'GUIDING':
                dg[gname] = str(gval)
        
        if dg['GUIDING'] == "NO":
            c = 0
            return c


        # Fetch AG calculation parameters

        raw   = subprocess.check_output(['get_status', 'PFS.AG'])
        #raw   = subprocess.check_output(['get_status', 'MEMORY.PFS.DUMMY_'])
        lines = raw.decode('latin-1').split('\n')

        d = {}
        for l in lines:
            if not l:
                continue
            name, val = l.split(':')
            name = name.strip()         # delete extra space
            name = name.split('.')[-1]  # extract last content
            val = val.strip()

            if name == 'EXPID':
            #if name == 'DUMMY_EXPID':
                d[name] = int(val)
            else:
                d[name] = float(val)

        # Check updates

        if d['EXPID'] == lastExpid:
        #if d['DUMMY_EXPID'] == lastExpid:
            time.sleep(3)
            continue

        # add most recent values to list

        lastExpid = d['EXPID']
        #lastExpid = d['DUMMY_EXPID']
        if linenum == 0:
            linenum += 1
            continue
        ln = np.append(ln, d['INR_ERR'])
        #ln = np.append(ln, d['DUMMY_INR_ERR'])

        # Calculate median

        # Calculate median and return median if it is exceeding the threshold

        inrerr_median = np.median(ln[-10:])
        c = 1 / inrerr_median

        # Calculate median and return median if it is exceeding the threshold and frame num > 10

        if linenum >= 10:
            if inrerr_median < thres_min or inrerr_median > thres_max:
                return c
        else:
            #print(c)
            linenum += 1

        time.sleep(3)




