"""
ID: thanhti1
LANG: PYTHON3
TASK: ride
"""

with open('ride.in', 'r') as fin:
    line_a = fin.readline().strip()
    line_b = fin.readline().strip()

def hask(line):
    result = 1
    for j in line:
        result *= ord(j) - 64
    result %= 47
    return result

if hask(line_a) == hask(line_b):
    out='GO\n'
else:
    out='STAY\n'

with open('ride.out', 'w') as fout:
    fout.write(out)