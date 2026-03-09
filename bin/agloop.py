import subprocess
import time
from itertools import cycle

def getAgRow():
    raw = subprocess.check_output(['get_status', 'PFS.AG'])
    lines = raw.decode('latin-1').split('\n')

    d = {}
    for l in lines:
        if not l:
            continue
        name, val = l.split(':')
        name = name.strip()
        name = name.split('.')[-1]
        val = val.strip()
        if name == 'EXPID':
            d[name] = int(val)
        elif name == 'STATUS':
            d[name] = val
        else:
            d[name] = float(val)

    return d
    
lastExpid = None
lineNum = 0
last_time = int(time.time())
time_old = 10
red='\033[31m'
red2='\033[91m'
magenta='\033[35m'
bgwhite='\33[107m'
bgcycle=cycle(['\33[107m', '\33[106m', '\33[103m'])
cyan='\033[96m'
face=cycle([' !!!!! ',' ----- '])

default='\033[0m'

while True:
    row = getAgRow()
    now_time = int(time.time())
    age = now_time - last_time
    if row['EXPID'] == lastExpid:
        if age > time_old:
            emoji = next(face)
            print(f'{red}{next(bgcycle)} {emoji}The last update was {age}s ago!{emoji} {default}',end='\r')
        continue
    lastExpid = row['EXPID']

    if age >= time_old:
        text_color = red2
    else:
        text_color = default
    if lineNum % 40 == 0:
        print(f'EXPID       ALT       AZ         RA      DEC        INR    FOCUS    SCALE  STATUS  AGE')

    print(f'{text_color}{row["EXPID"]:-5d} {row["ALT_ERR"]: 8.3f} {row["AZ_ERR"]: 8.3f}'
          f'   {row["RA_ERR"]: 8.3f} {row["DEC_ERR"]: 8.3f}'
          f'   {row["INR_ERR"]: 8.3f} {row["FOCUS_ERR"]: 8.3f} {row["SCALE_ERR"]*1000: 8.3f}'
          f'   {row.get("STATUS")}     {age:2d}s{default}')

    lineNum += 1
    last_time = now_time
    
    time.sleep(1)
    
