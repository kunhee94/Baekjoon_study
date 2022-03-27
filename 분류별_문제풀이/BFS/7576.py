import sys
from collections import deque
sys.stdin = open("input.txt", "r")

# M, N = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# visited = [[0]*M for _ in range(N)]
# # 토마토가 여러개면 전부 Q에 넣고 시작해버리면됨
# Q = []
# for x in range(N):
#     for y in range(M):
#         if arr[x][y] == 1:
#             Q.append((x,y))
#             # 출발할 곳 미리 표시
#             visited[x][y] = 1
#             # 못갈곳 미리 표시
#         elif arr[x][y] == -1:
#             visited[x][y] = -1
# while Q:
#     cx, cy = Q.pop(0)
#     for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
#         nx = dx + cx
#         ny = dy + cy
#         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0 and visited[nx][ny] == 0:
#             Q.append((nx, ny))
#             visited[nx][ny] = visited[cx][cy] + 1
#
# res = []
# for x in range(N):
#     res.append(max(visited[x]))
#     if 0 in visited[x]:
#         print(-1)
#         break
# else:
#     print(max(res)-1)

# deque 안써서 틀림 백준 풀때 q쓸꺼면 deque 호출해서 쓰자
M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Q = deque()
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            Q.append((x,y))
while Q:
    cx, cy = Q.popleft()
    for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
        nx = dx + cx
        ny = dy + cy
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            Q.append((nx, ny))
            arr[nx][ny] = arr[cx][cy] + 1
res = []
for x in range(N):
    res.append(max(arr[x]))
    if 0 in arr[x]:
        print(-1)
        break
else:
    print(max(res)-1)