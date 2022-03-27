import sys
sys.stdin = open("input.txt", "r")


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

sx = sy = 0

Q = []
Q.append((sx, sy))
visited = [[0]*M for _ in range(N)]
visited[0][0] = 1
while Q:
    cx, cy = Q.pop(0)
    for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
        nx =  dx + cx
        ny =  dy + cy
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny]:
            visited[nx][ny] = visited[cx][cy] + 1
            if nx == N-1 and ny == M-1:
                print(visited[nx][ny])
                break
            else:
                Q.append((nx, ny))

