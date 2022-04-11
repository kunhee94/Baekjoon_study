import sys
from collections import deque
sys.stdin = open("input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(sx,sy):
    global check
    Q = deque()
    Q.append((sx, sy))
    visited[sx][sy] = 1
    cont = [(sx,sy)]
    while Q:
        cx, cy = Q.popleft()
        for k in range(4):
            nx = cx +dx[k]
            ny = cy +dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0  and L <= abs(arr[nx][ny]-arr[cx][cy]) <= R:
                visited[nx][ny] = 1
                cont.append((nx, ny))
                Q.append((nx,ny))
    return cont


N, L, R = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
cnt = 0
# 매일 새로 갱신해서 확인해야됨
while True:
    visited = [[0] * N for _ in range(N)]
    # 인구이동 없었을 때 while문 정지하기 위한 변수
    a = 1
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                res = BFS(x,y)
                # 연합이 만들어졋으면 인구이동 시켜주기
                if len(res) > 1:
                    num = sum([arr[i][j] for i, j in res]) // len(res)
                    a = 0
                    for i,j in res:
                        arr[i][j] = num
    # 인구이동 없으면 정지
    if a:
        break
    # 있었으면 날짜 증가 시켜주고 또 옮겨야되나 확인하러
    cnt += 1

print(cnt)









