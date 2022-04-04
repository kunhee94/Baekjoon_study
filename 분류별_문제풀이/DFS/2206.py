import sys
from collections import deque
sys.stdin =open("input.txt", "r")

dx = [1,-1,0,0]
dy = [0,0,-1,1]

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# 0, 0 부터 N-1, M-1까지 가야함
res = 99999999
# 방문 배열
visited = [[0]*M for _ in range(N)]
Q = deque()
# 시작점, 이동횟수, 벽부순횟수
Q.append([0,0,0])
visited[0][0] = 1
while Q:
    cx, cy, how = Q.popleft()
    if cx == N - 1 and cy == M - 1:
        res = visited[cx][cy]
        break
    for k in range(4):
        nx = cx + dx[k]
        ny = cy + dy[k]
        # 인덱스 범위 내이고 방문하지 않았을때
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            # 벽이면 벽을 아직 한번도 안부쉇을 때만 부수고 가기 가능
            if arr[nx][ny] and how == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                # 벽 1번 부쉇다고 표시하고 q에 넣음
                Q.append([nx, ny, how + 1])
            # 벽이 아닐때
            elif arr[nx][ny] == 0 and how <= 1:
                visited[nx][ny] = visited[cx][cy] + 1
                Q.append([nx, ny, how])
if res == 99999999:
    print(-1)
else:
    print(res)

