import sys
from collections import deque
sys.stdin =open("input.txt", "r")

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
#
# N, M = map(int, sys.stdin.readline().rstrip().split())
# arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# 0, 0 부터 N-1, M-1까지 가야함
# res = 99999999
# # 방문 배열
# visited = [[0]*M for _ in range(N)]
# Q = deque()
# # 시작점, 이동횟수, 벽부순횟수
# Q.append([0,0,0])
# visited[0][0] = 1
# while Q:
#     cx, cy, how = Q.popleft()
#     if cx == N - 1 and cy == M - 1:
#         res = visited[cx][cy]
#         break
#     for k in range(4):
#         nx = cx + dx[k]
#         ny = cy + dy[k]
#         # 인덱스 범위 내이고 방문하지 않았을때
#         if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
#             # 벽이면 벽을 아직 한번도 안부쉇을 때만 부수고 가기 가능
#             if arr[nx][ny] and how == 0:
#                 visited[nx][ny] = visited[cx][cy] + 1
#                 # 벽 1번 부쉇다고 표시하고 q에 넣음
#                 Q.append([nx, ny, how + 1])
#             # 벽이 아닐때
#             elif arr[nx][ny] == 0 and how <= 1:
#                 visited[nx][ny] = visited[cx][cy] + 1
#                 Q.append([nx, ny, how])
# if res == 99999999:
#     print(-1)
# else:
#     print(res)



row, col = map(int, input().split())
graph = [list(map(int, input())) for _ in range(row)]
visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def Bfs(start_x, start_y, iscrash, visited, graph):
    #crash 0: 벽안부시고 가는경우, 1: 부신 경우
    queue = deque()
    queue.append((start_x, start_y, iscrash))
    visited[start_x][start_y][iscrash] = 1

    while queue:
        cur_x, cur_y, iscrash = queue.popleft()
        if cur_x == row - 1 and cur_y == col - 1:
            return visited[cur_x][cur_y][iscrash]
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x <= -1 or next_x >= row or next_y <= -1 or next_y >= col:
                continue
            # 벽 안부수고 이동
            if graph[next_x][next_y] == 0 and visited[next_x][next_y][iscrash] == 0:
                queue.append((next_x, next_y, iscrash))
                visited[next_x][next_y][iscrash] = visited[cur_x][cur_y][iscrash] + 1
            # 벽 부수고 이동
            if graph[next_x][next_y] == 1 and iscrash == 0:
                queue.append((next_x, next_y, iscrash + 1))
                visited[next_x][next_y][iscrash + 1] = visited[cur_x][cur_y][iscrash] + 1

    return -1

print(Bfs(0, 0, 0, visited, graph))