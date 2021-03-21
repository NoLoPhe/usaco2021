"""
ID: thanhti1
LANG: PYTHON3
TASK: ride
"""

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

contents = fin.read().split()
kt = 0
for i in contents:
    mod = 1
    for j in i:
        mod *= ord(j) - 64
    mod %= 47
    if not kt:
        kt = mod
    else:
        if kt == mod:
            fout.write('GO' + '\n')
        else:
            fout.write('STAY'+ '\n')
        break
fout.close()