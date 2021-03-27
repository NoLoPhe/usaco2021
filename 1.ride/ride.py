"""
ID: thanhti1
LANG: PYTHON3
TASK: ride
"""

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

line_a = fin.readline().replace('\n','')
line_b = fin.readline().replace('\n','')

def hask(line):
    result = 1
    for j in line:
        result *= ord(j) - 64
    result %= 47
    return result

if hask(line_a) == hask(line_b):
    fout.write('GO\n')
else:
    fout.write('STAY\n')
fout.close()
