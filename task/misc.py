import math
import re

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

def random_song(music1,music2,music3):
    import random
    song = [music1,music2,music3]    
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
