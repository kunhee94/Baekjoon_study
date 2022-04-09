import sys
sys.stdin =open("input.txt", "r")


dx = [1,-1,0,0]
dy = [0,0,-1,1]

def DFS(sx,sy):
    if sx == N-1 and sy == M-1:
        return 1
    # 방문했던 곳이면 지금 저장 되어있는 dp가져오기
    if visited[sx][sy] != -1:
        return visited[sx][sy]
    visited[sx][sy] = 0
    for k in range(4):
         nx = sx + dx[k]
         ny = sy + dy[k]
         # 내리막길로만 이동
         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] < arr[sx][sy]:
             visited[sx][sy] += DFS(nx, ny)
    return visited[sx][sy]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
print(DFS(0,0))