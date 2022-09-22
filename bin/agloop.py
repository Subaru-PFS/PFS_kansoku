import subprocess
import time

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
        else:
            d[name] = float(val)

    return d
    
lastExpid = None
lineNum = 0
while True:
    row = getAgRow()
    if row['EXPID'] == lastExpid:
        continue
    lastExpid = row['EXPID']

    if lineNum % 40 == 0:
        print(f'EXPID    ALT    AZ       RA     DEC      INR    FOCUS')

    print(f'{row["EXPID"]:-5d} {row["ALT_ERR"]: 7.3f} {row["AZ_ERR"]: 6.3f}'
          f'   {row["RA_ERR"]: .3f} {row["DEC_ERR"]: 6.3f}'
          f'   {row["INR_ERR"]: 6.3f} {row["FOCUS_ERR"]: 6.3f}')

    lineNum += 1
    
    time.sleep(1)
    
