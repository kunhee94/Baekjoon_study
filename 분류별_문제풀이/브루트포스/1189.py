import sys
sys.stdin =open("input.txt", "r")

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def DFS(x,y,cnt):
    global res
    if cnt > K:
        return
    if x == 0 and y == M-1:
        if cnt == K-1:
            res += 1
        return
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N  and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] != 'T':
            visited[nx][ny] = 1
            DFS(nx,ny,cnt+1)
            visited[nx][ny] = 0


N, M, K = map(int, input().split())

arr = [input()for _ in range(N)]
visited = [[0]*M for _ in range(N)]
start_x = N-1
start_y = 0
res = 0
visited[start_x][start_y] = 1
DFS(start_x,start_y,0)
print(res)
