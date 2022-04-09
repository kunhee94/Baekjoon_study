import sys
sys.stdin =open("input.txt", "r")


n = int(input())
stack = []
res = []
cnt = 1
temp = 1
for i in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        res.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        res.append('-')
    else:
        temp = 0
        break
if temp == 0:
    print('NO')
else:
    for i in res:
        print(i)



















