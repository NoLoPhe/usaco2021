"""
ID: thanhti1
LANG: PYTHON3
TASK: friday
"""

#O(n)
with open('friday.in', 'r') as fin:
    year = int(fin.readline().strip())

month = [31,28,31,30,31,30,31,31,30,31,30,31]
cnt = {i:0 for i in range(7)}
cur = 13

for i in range(1900, 1900+year):
    for m in month:
        cnt[(cur%7+1)%7] += 1 #Cursor cur contro
        if m==28:
            # if (i % 400 == 0 or (i % 100 != 0 and i % 4 == 0)): #y%4==0 && (y%100 != 0 || y%400 == 0);
            if i%4==0 and (i%100!=0 or i%400==0):
                cur += 1    #28+1
        cur += m

output = ''
for i in cnt:
    if i == 6:
        output += str(cnt[i]) + '\n'
    else:
        output += str(cnt[i]) + ' '

with open('friday.out', 'w') as fout:
    fout.write(output)

#440 439 438 438 439 439 439