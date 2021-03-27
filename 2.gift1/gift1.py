"""
ID: thanhti1
LANG: PYTHON3
TASK: gift1
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

np = int(fin.readline())
names = {}
for i in range(np):
    names[fin.readline().replace("\n", "")]=0
for i in names:
    sender = fin.readline().replace("\n", "")
    amount, num_people = map(int, fin.readline().split())
    if num_people == 0:
        continue
    moneyGot= amount//num_people
    names[sender] = names[sender] - amount + amount%num_people
    for i in range(num_people):
        receiver = fin.readline().replace("\n", "")
        names[receiver] += moneyGot
for i in names:
    fout.write(i + ' ' + str(names[i]) + '\n')
fout.close()