"""
ID: thanhti1
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in','r')
fout = open('friday.out','w')
month=[31,28,31,30,31,30,31,31,30,31,30,31]
i = int(fin.readline())
A={i:0 for i in range(7)}
day = 13
for y in range(1900, 1900+i):
    # if y%100==0:
    #     if y%400==0:
    #         t2 = 29
    #     else:
    #         t2 = 28
    # elif y%4==0:
    #     t2 = 29
    # else:
    #     t2 = 28
    # if (y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)):
    for m in month:
        # thu = ((365 * (y - 1900 - (0 if y<1901 else (y - 1901)//4)) + 366 * (0 if y<1901 else (y - 1901)//4) + day) % 7 + 1)%7
        A[(day%7+1)%7] += 1
        if m==28:
            if (y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)):
                day += 29
                continue
        day += m
for i in A:
    if i==6:
        fout.write(str(A[i]) + '\n')
    else:
        fout.write(str(A[i]) +' ')
fout.close()

# with open('friday.out','w') as fout:
# 	for day in range(6):
# 		fout.write("{} ".format(dayOfWeeks[day]))
# 	fout.write("{}\n".format(dayOfWeeks[6]))