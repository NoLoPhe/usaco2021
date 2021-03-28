"""
ID: thanhti1
LANG: PYTHON3
TASK: beads
"""

# code1 O(2n)
with open('beads.in', 'r') as fin:
    n = int(fin.readline().strip())
    A = list(fin.readline().strip())

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

# Test 1: TEST OK [0.024 secs, 9296 KB]
# Test 2: TEST OK [0.024 secs, 9420 KB]
# Test 3: TEST OK [0.025 secs, 9380 KB]
# Test 4: TEST OK [0.025 secs, 9356 KB]
# Test 5: TEST OK [0.024 secs, 9336 KB]
# Test 6: TEST OK [0.024 secs, 9320 KB]
# Test 7: TEST OK [0.025 secs, 9348 KB]
# Test 8: TEST OK [0.025 secs, 9460 KB]
# Test 9: TEST OK [0.028 secs, 9504 KB]

# #code2 O(n^2)
# with open('beads.in', 'r') as fin:
#     size = int(fin.readline().strip())
#     A = list(fin.readline().strip())
#
# def n_break(i, dir):
#     color = 'w'
#     if dir > 0: #negative direction
#         i = i
#     else:       #positive direction
#         i = (i+dir)%size
#     for n in range(size):
#         if color=='w' and A[i]!='w':
#             color=A[i]
#         elif color!='w' and A[i]!='w' and A[i]!=color:
#             break
#         i = (i+dir)%size    #direction
#     return n
#
# ans=0
# for i in range(size):
#     n = n_break(i,1) + n_break(i,-1)
#     ans = max(ans,n)
# ans = min(ans, size)
#
# with open('beads.out', 'w') as fout:
#     fout.write(str(ans) + '\n')

# Test 1: TEST OK [0.029 secs, 9372 KB]
# Test 2: TEST OK [0.024 secs, 9320 KB]
# Test 3: TEST OK [0.025 secs, 9360 KB]
# Test 4: TEST OK [0.025 secs, 9308 KB]
# Test 5: TEST OK [0.024 secs, 9420 KB]
# Test 6: TEST OK [0.024 secs, 9348 KB]
# Test 7: TEST OK [0.027 secs, 9416 KB]
# Test 8: TEST OK [0.025 secs, 9328 KB]
# Test 9: TEST OK [0.025 secs, 9312 KB]

# #code3 O(2n)
# with open('beads.in', 'r') as fin:
#     n = int(fin.readline().strip())
#     A = list(fin.readline().strip())
#
# A = A + A
# ans=0
# for i in range(n):
#     check = A[i]
#     print(check)
#     if check=='w':
#         state = 0
#     else:
#         state = 1
#     j=i
#     current = 0
#     while state <=2:
#         while j < n+i and (A[j]=='w' or A[j]==check):
#             j+=1
#             current +=1
#             # print(A[j])
#         check=A[j]
#         state+=1
#     # print(str(current)+'\n')
#     ans = max(ans,current)
#
# with open('beads.out', 'w') as fout:
#     fout.write(str(ans) + '\n')

# Test 1: TEST OK [0.025 secs, 9312 KB]
# Test 2: TEST OK [0.024 secs, 9352 KB]
# Test 3: TEST OK [0.027 secs, 9416 KB]
# Test 4: TEST OK [0.025 secs, 9232 KB]
# Test 5: TEST OK [0.025 secs, 9312 KB]
# Test 6: TEST OK [0.025 secs, 9344 KB]
# Test 7: TEST OK [0.034 secs, 9280 KB]
# Test 8: TEST OK [0.031 secs, 9316 KB]
# Test 9: TEST OK [0.032 secs, 9232 KB]

# ------- test 1 [length 33 bytes] ----
# 29
# wwwbbrwrbrbrrbrbrwrwwrbwrwrrb
# ------- test 2 [length 6 bytes] ----
# 3
# rrr
# ------- test 3 [length 81 bytes] ----
# 77
# rwrwrwrwrwrwrwrwrwrwrwrwbwrwbwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwr
# ------- test 4 [length 21 bytes] ----
# 17
# wwwwwwwwwwwwwwwww
# ------- test 5 [length 54 bytes] ----
# 50
# bbrrrbrrrrrrrrbrbbbrbrrbrrrrbbbrbrbbbbbrbrrrbbrbbb
# ------- test 6 [length 11 bytes] ----
# 8
# rrwwwwbb
# ------- test 7 [length 205 bytes] ----
# 200
# rrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbb
# ------- test 8 [length 355 bytes] ----
# 350
# rrbbrbbbwbwwbwbbbbwwrrbbwbrwbrwbbbrbrwrwbrwwwrrbbrrwrbbrwbwrwwwrbrwwwwwrwbwwwrrbrrbbbrbrbbbrbbbrbbwbbbbbrbrrbrwwbrrrrwbwrwrbbwbwrbrbrwwbrrbwbrwwbwwwbrbwrwbwbrbbbwrbwwrrrbwbwbbbbbrrwwwrbrwwrbbwrbbrbbrbwrrwwbrrrbrwbrwwrbwbwrrrbwrwrrbrbbwrwrbrwwwrwbwrrwwwwrrrwrrwbbwrwwrwrbwwbwrrrrbbwrbbrbwwwwwbrbbrbbrbrwbbwbwwbbbbbwwwrbwwbbbwrwwbbrrwrwbwrrwwwrrrwrrwww
# ------- test 9 [length 338 bytes] ----
# 333
# rwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwbrwb
