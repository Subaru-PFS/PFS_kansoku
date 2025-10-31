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
        elif name == 'STATUS':
            d[name] = val
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
        print(f'EXPID       ALT       AZ         RA      DEC        INR    FOCUS    SCALE  STATUS')

    print(f'{row["EXPID"]:-5d} {row["ALT_ERR"]: 8.3f} {row["AZ_ERR"]: 8.3f}'
          f'   {row["RA_ERR"]: 8.3f} {row["DEC_ERR"]: 8.3f}'
          f'   {row["INR_ERR"]: 8.3f} {row["FOCUS_ERR"]: 8.3f} {row["SCALE_ERR"]*1000: 8.3f}'
          f'   {row.get("STATUS")}')

    lineNum += 1
    
    time.sleep(1)
    
