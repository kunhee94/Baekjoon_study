import sys
from collections import deque
sys.stdin = open("input.txt", "r")
T = int(input())
def BFS(sx, sy):
    Q = deque()
    Q.append((sx,sy))
    visited[sx][sy] = 1
    while Q:
        cx, cy = Q.popleft()
        for k in range(8):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                Q.append((nx,ny))
                visited[nx][ny] = visited[cx][cy] + 1
                if nx == tx and ny == ty:
                    res.append(visited[nx][ny])
# 나이트 이동
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    start_x, start_y = map(int, input().split())
    tx, ty = map(int, input().split())
    res = []
    BFS(start_x,start_y)
    if res:
        print(min(res)-1)
    else:
        print(0)

