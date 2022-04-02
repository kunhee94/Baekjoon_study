import sys
from collections import deque
sys.stdin =open("input.txt", "r")



dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

def DFS(sx,sy):
    for k in range(8):
        nx = sx+dx[k]
        ny = sy+dy[k]
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            DFS(nx, ny)

def BFS(sx,sy):
    Q = deque()
    Q.append((sx,sy))
    while Q:
        cx, cy = Q.popleft()
        for k in range(8):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                Q.append((nx, ny))
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for x in range(h):
        for y in range(w):
            if arr[x][y] and visited[x][y] == 0:
                visited[x][y] = 1
                # DFS(x, y)
                BFS(x, y)
                cnt += 1
    print(cnt)


