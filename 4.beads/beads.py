"""
ID: thanhti1
LANG: PYTHON3
TASK: beads
"""

with open('beads.in', 'r') as fin:
    raw_line = fin.readlines()

n = int(raw_line.pop(0).strip())
A = list(raw_line.pop(0).strip().replace('\n',''))

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

ans=0
for i in range(1,len(A)-1):
    ans=max(ans,max(left[i][0], left[i][1]+right[i+1][0], left[i][0]+right[i+1][1], right[i+1][1]))
ans=min(ans,n)

with open('beads.out', 'w') as fout:
    fout.write(str(ans) + '\n')

