import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def BFS(sx,sy):
    Q = deque()
    visited = [[0]*M for _ in range(N)]
    visited[sx][sy] = 1
    Q.append((sx,sy))
    cnt = 0
    while Q:
        cx,cy = Q.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N  and 0 <= ny < M  and visited[nx][ny] == 0 and arr[nx][ny] == 'L':
                visited[nx][ny] = visited[cx][cy] + 1
                Q.append((nx,ny))
                cnt = visited[nx][ny] - 1
    return cnt



N, M = map(int, input().split())

arr = [list(sys.stdin.readline().rstrip())for _ in range(N)]

res = 0

for x in range(N):
    for y in range(M):
        if arr[x][y] == 'L':
            a = BFS(x,y)
            if res < a:
                res = a
print(res)