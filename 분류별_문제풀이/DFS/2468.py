import sys
sys.setrecursionlimit(1010000)
sys.stdin =open("input.txt", "r")


dx = [1,-1,0,0]
dy = [0,0,-1,1]

def DFS(sx, sy):
    for k in range(4):
        nx = sx + dx[k]
        ny = sy + dy[k]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > i and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            DFS(nx, ny)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt_lis = []
k = max(max(arr))
for i in range(k):
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0 and arr[x][y]> i:
                visited[x][y] = 1
                DFS(x, y)
                cnt += 1
    cnt_lis.append(cnt)
print(max(cnt_lis))



