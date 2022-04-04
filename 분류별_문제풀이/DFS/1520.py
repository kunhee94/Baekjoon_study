import sys
from collections import deque
sys.stdin =open("input.txt", "r")

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
#
# def DFS(sx, sy):
#     global cnt
#     if sx == N-1 and sy == M-1:
#         cnt += 1
#         return
#     for k in range(4):
#         nx = sx + dx[k]
#         ny = sy + dy[k]
#         if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[sx][sy] > arr[nx][ny]:
#             visited[nx][ny] = 1
#             DFS(nx, ny)
#             visited[nx][ny] = 0
# N, M = map(int,sys.stdin.readline().rstrip().split())
# arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
# cnt = 0
# visited = [[0]*M for _ in range(N)]
# DFS(0,0)
# print(cnt)


# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
#
# def DFS(sx, sy):
#     global cnt
#     if sx == N-1 and sy == M-1:
#         cnt += 1
#         return
#     for k in range(4):
#         nx = sx + dx[k]
#         ny = sy + dy[k]
#         if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[sx][sy] > arr[nx][ny]:
#             visited[nx][ny] = 1
#             DFS(nx, ny)
#             visited[nx][ny] = 0
# N, M = map(int,sys.stdin.readline().rstrip().split())
# arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
# cnt = 0
# lis = []
# visited = [[0]*M for _ in range(N)]
# DFS(0,0)
# print(cnt)

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
#
# def DFS(sx, sy):
#     global cnt
#     if sx == N-1 and sy == M-1:
#         cnt += 1
#         return
#     for k in range(4):
#         nx = sx + dx[k]
#         ny = sy + dy[k]
#         if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[sx][sy] > arr[nx][ny]:
#             visited[nx][ny] = 1
#             DFS(nx, ny)
#             visited[nx][ny] = 0
# N, M = map(int,sys.stdin.readline().rstrip().split())
# arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
# cnt = 0
# visited = [[0]*M for _ in range(N)]
# DFS(0,0)
# print(cnt)


# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
#
# def DFS(sx, sy):
#     global cnt
#     if sx == N-1 and sy == M-1:
#         cnt += 1
#         return
#     for k in range(4):
#         nx = sx + dx[k]
#         ny = sy + dy[k]
#         if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[sx][sy] > arr[nx][ny]:
#             visited[nx][ny] = 1
#             DFS(nx, ny)
#             visited[nx][ny] = 0
# N, M = map(int,sys.stdin.readline().rstrip().split())
# arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
# cnt = 0
# lis = []
# visited = [[0]*M for _ in range(N)]
# DFS(0,0)
# print(cnt)



dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if s[x][y] < s[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]
m, n = map(int, input().split())
s = [list(map(int, input().split())) for i in range(m)]
dp = [[-1] * n for i in range(m)]
print(dfs(m - 1, n - 1))