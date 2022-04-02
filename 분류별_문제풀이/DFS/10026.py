import sys
sys.setrecursionlimit(1010000)
sys.stdin =open("input.txt", "r")


dx = [1,-1,0,0]
dy = [0,0,-1,1]

def DFS(sx, sy):
    if arr[sx][sy] == 'R':
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            # 색깔이 빨강이고 방문한적 없으면
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'R' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                DFS(nx,ny)
    elif arr[sx][sy] == 'B':
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            # 색깔이 빨강이고 방문한적 없으면
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'B' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                DFS(nx,ny)
    elif arr[sx][sy] == 'G':
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            # 색깔이 빨강이고 방문한적 없으면
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'G' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                DFS(nx,ny)

def DFS2(sx, sy):
    if arr[sx][sy] == 'R' or arr[sx][sy] == 'G':
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            # 색깔이 빨강이고 방문한적 없으면
            if 0 <= nx < N and 0 <= ny < N and visited_2[nx][ny] == 0 and (arr[nx][ny] == 'R' or arr[nx][ny] == 'G'):
                visited_2[nx][ny] = 1
                DFS2(nx,ny)
    elif arr[sx][sy] == 'B':
        for k in range(4):
            nx = sx + dx[k]
            ny = sy + dy[k]
            # 색깔이 빨강이고 방문한적 없으면
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'B' and visited_2[nx][ny] == 0:
                visited_2[nx][ny] = 1
                DFS2(nx,ny)


N = int(sys.stdin.readline().rstrip())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited_2 = [[0]*N for _ in range(N)]
cnt = 0
cnt_2 = 0
for x in range(N):
    for y in range(N):
        if visited[x][y] == 0:
            visited[x][y] = 1
            DFS(x, y)
            cnt += 1
        if visited_2[x][y] == 0:
            visited_2[x][y] = 1
            DFS2(x, y)
            cnt_2 += 1
print(cnt, cnt_2)

