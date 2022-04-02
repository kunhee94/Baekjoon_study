import sys
sys.setrecursionlimit(1010000)
sys.stdin =open("input.txt", "r")

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def DFS(sx, sy, cnt, how):
    global res
    if res < cnt:
        return
    if sx == N-1 and sy == M-1:
        res = cnt
    for k in range(4):
        nx = sx + dx[k]
        ny = sy + dy[k]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
        # 벽안부술때
            if arr[nx][ny] == 0:
                visited[nx][ny] = 1
                DFS(nx, ny, cnt + 1, how)
                visited[nx][ny] = 0
            # 벽을 아직 한번도 안부쉇을 때만 부수고 가기 가능
            elif arr[nx][ny] and how == 0:
                visited[nx][ny] = 1
                DFS(nx, ny, cnt + 1, how + 1)
                visited[nx][ny] = 0

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# 0, 0 부터 N-1, M-1까지 가야함
res = 99999999
visited = [[0]*M for _ in range(N)]
DFS(0,0,0,0)
if res == 99999999:
    print(-1)
else:
    print(res+1)