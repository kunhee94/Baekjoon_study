import sys
sys.setrecursionlimit(1010000)
sys.stdin =open("input.txt", "r")


dx = [1,-1,0,0]
dy = [0,0,-1,1]

def DFS(sx, sy):
    global cnt
    for k in range(4):
        nx = sx + dx[k]
        ny = sy + dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            cnt += 1
            DFS(nx, ny)


N, M, K = map(int, sys.stdin.readline().rstrip().split())
arr = [[1] * M for _ in range(N)]
info = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
for i in info:
    # 왼쪽아래 = arr[N-y_1-1][x_1] 오른쪽위 = arr[N-y_2][x_2]
    x_1, y_1, x_2, y_2 = i
    # 위부터 아래로
    for k in range(N-y_2, N-y_1):
        # 좌부터 우로
        for p in range(x_1, x_2):
            arr[k][p] = 0
visited = [[0]*M for _ in range(N)]
res = 0
cnt_lis = []
for x in range(N):
    for y in range(M):
        # 색칠 안했고 방문안했으면
        if arr[x][y] and visited[x][y] == 0:
            cnt = 1
            visited[x][y] =1
            res += 1
            DFS(x, y)
            cnt_lis.append(cnt)
print(res)
print(*sorted(cnt_lis))
