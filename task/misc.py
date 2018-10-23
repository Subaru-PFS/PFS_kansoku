import math

## sybbolic link from $OBSHOME/COMMON/pfsmisc.py to this file
def adc_pos(el,cnf):

    e={"WAVE9":[0.0027, 12.6755, -0.0992, 0.2141, -0.0901]}

    za=(90-el)*math.pi/180.

    t=math.tan(za)

    if cnf in e:
        pos=e[cnf][0] + e[cnf][1]*t + e[cnf][2]*math.pow(t,2) + e[cnf][3]*math.pow(t,3) +e[cnf][4]*math.pow(t,4)
    else:
        pos=-99.

    return pos
