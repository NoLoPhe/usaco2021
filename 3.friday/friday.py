"""
ID: thanhti1
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in','r')
fout = open('friday.out','w')

month = [31,28,31,30,31,30,31,31,30,31,30,31]
cnt = {i:0 for i in range(7)}
cur = 13

year = int(fin.readline())
for i in range(1900, 1900+year):
    for m in month:
        cnt[(cur%7+1)%7] += 1 #Cursor cur contro
        if m==28:
            if (i % 400 == 0 or (i % 100 != 0 and i % 4 == 0)):
                cur += 29
                continue
        cur += m

for i in cnt:
    if i==6:
        fout.write(str(cnt[i]) + '\n')
    else:
        fout.write(str(cnt[i]) +' ')
fout.close()

#440 439 438 438 439 439 439