import sys
from collections import deque
sys.stdin =open("input.txt", "r")

dx = [1,-1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]


def BFS(sx,sy):
    visited = [[0]*M for _ in range(N)]
    Q = deque()
    Q.append((sx,sy))
    visited[sx][sy] = 1
    while Q:
        cx,cy = Q.popleft()
        for k in range(8):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M  and visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                if arr[nx][ny]:
                    return visited[nx][ny] - 1
                Q.append((nx,ny))


N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
res = 0

for x in range(N):
    for y in range(M):
        if not arr[x][y]:
            how_far = BFS(x,y)
            if how_far > res:
                res = how_far
print(res)