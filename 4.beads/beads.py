"""
ID: thanhti1
LANG: PYTHON3
TASK: beads
"""

fin=open('beads.in','r')
fout=open('beads.out','w')

n = int(fin.readline())
A = list(fin.readline().replace('\n',''))

A = [' '] + A + A + [' ']
left = [[0,0] for i in range(len(A))] #[r,b]
for i in range(1,len(A)-1):
    if A[i]=='r':
        left[i][0] = left[i-1][0] + 1
        left[i][1] = 0
    elif A[i] == 'b':
        left[i][1] = left[i-1][1] + 1
        left[i][0] = 0
    elif A[i] == 'w':
        left[i][0] = left[i - 1][0] + 1
        left[i][1] = left[i - 1][1] + 1

right = [[0,0] for i in range(len(A))] #[r,b]
for i in range(1,len(A)-1):
    i = len(A)-1-i
    if A[i]=='r':
        right[i][0] = right[i+1][0] + 1
        right[i][1] = 0
    elif A[i] == 'b':
        right[i][1] = right[i+1][1] + 1
        right[i][0] = 0
    elif A[i] == 'w':
        right[i][0] = right[i + 1][0] + 1
        right[i][1] = right[i + 1][1] + 1

# print(left)
# print(right)

ans=0
for i in range(1,len(A)-1):
    ans=max(ans,max(left[i][0], left[i][1]+right[i+1][0], left[i][0]+right[i+1][1], right[i+1][1]))
ans=min(ans,n)

fout.write(str(ans) + '\n')
fout.close()

