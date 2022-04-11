import sys
from collections import deque
sys.stdin = open("input.txt", "r")

F, S, G, U, D = map(int, sys.stdin.readline().rstrip().split())
visited = [0]*(F+1)
Q = deque()
Q.append((S, 0))
visited[S] = 1
res = 99999
while Q:
    s, cnt = Q.popleft()
    if s == G:
        res = cnt
        break
    for k in [s-D, s+U]:
        if 1 <= k <= F and visited[k] == 0:
            Q.append((k,cnt+1))
            visited[k] = 1
if res == 99999:
    print('use the stairs')
else:
    print(res)