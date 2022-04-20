import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx = [0,0,-1,1]
dy = [1,-1,0,0]



N, M = map(int, input().split())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

res = []
while True:
    visited = [[0]*M for _ in range(N)]
    Q = deque()
    Q.append((0,0))
    visited[0][0] = 1
    cnt = 0
    while Q:
        cx, cy = Q.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 공기면 Q에 넣음
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    Q.append((nx,ny))
                # 공기와 맞닿은 치즈면 0으로 바꾸고 갯수추가해주고 Q에 안넣어서 안쪽으로 진입을 막음
                else:
                    arr[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt += 1
    res.append(cnt)
    if cnt == 0:
        break
print(len(res)-1)
print(res[-2])
