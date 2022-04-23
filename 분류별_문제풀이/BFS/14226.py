import sys
from collections import deque
sys.stdin = open("input.txt","r")

S = int(input())

Q = deque()
Q.append((1, 0, 0))
res = 0
visited = [[0]*1001 for _ in range(1001)]
visited[1][0] = 1
while Q:
    now, clib, time = Q.popleft()
    if now == S:
        res = time
        break
    if now+clib <= 1000:
        # 복사 저장
        if visited[now][now] == 0:
            Q.append((now, now, time+1))
            visited[now][now] = 1
        # 붙여넣기
        if clib != 0 and visited[now+clib][clib] == 0:
            visited[now + clib][clib] = 1
            Q.append((now+clib, clib, time+1))
        if now-1 >= 0 and visited[now-1][clib] == 0:
            visited[now - 1][clib] = 1
            Q.append((now-1, clib, time+1))

print(res)