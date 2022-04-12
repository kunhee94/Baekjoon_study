import sys
from collections import deque
sys.stdin =open("input.txt", "r")


A, B = map(int, input().split())
res = 0
Q = deque()
Q.append((A,0))
while Q:
    now, cnt = Q.popleft()
    if now > B:
        continue
    if now == B:
        res = cnt + 1
    # 2를 곱할때
    new = now * 2
    Q.append((new, cnt+1))
    # 1을 추가
    new = now*10 + 1
    Q.append((new, cnt+1))
if res:
    print(res)
else:
    print(-1)
