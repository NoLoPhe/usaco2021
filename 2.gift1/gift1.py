"""
ID: thanhti1
LANG: PYTHON3
TASK: gift1
"""

with open('gift1.in', 'r') as fin:
    raw_line = fin.readlines()

np = int(raw_line.pop(0).strip())
names = {}
for i in range(np):
    names[raw_line.pop(0).strip()]=0

for i in names:
    giver = raw_line.pop(0).strip()
    amount, num_people = map(int, raw_line.pop(0).strip().split())
    if num_people == 0:
        continue
    moneyGot= amount//num_people
    names[giver] = names[giver] - amount + amount%num_people
    for i in range(num_people):
        receiver = raw_line.pop(0).strip()
        names[receiver] += moneyGot

out=''
for i in names:
    out += i + ' ' + str(names[i]) + '\n'

with open('gift1.out', 'w') as fout:
    fout.write(out)