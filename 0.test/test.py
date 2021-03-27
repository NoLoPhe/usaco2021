"""
ID: thanhti1
LANG: PYTHON3
TASK: test
"""
with open('test.in', 'r') as fin:
    raw_line = fin.readline()

x, y = map(int, raw_line.split())
sum = x + y

with open('test.out', 'w') as fout:
    fout.write(str(sum) + '\n')