"""
ID: thanhti1
LANG: PYTHON3
TASK: gift1
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

np = int(fin.readline())
dic = {}
for i in range(np):
    dic[fin.readline().replace("\n", "")]=0
for i in dic:
    name_gi = fin.readline().replace("\n", "")
    dola, numsend = map(int, fin.readline().split())
    if numsend == 0:
        continue
    dola_= dola//numsend
    dic[name_gi] = dic[name_gi] - dola + dola%numsend
    for i in range(numsend):
        name_re = fin.readline().replace("\n", "")
        dic[name_re] += dola_
for i in dic:
    fout.write(i + ' ' + str(dic[i]) + '\n')
fout.close()