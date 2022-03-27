import sys
sys.stdin = open("input.txt", "r")

N = int(input())

arr = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
res_1 = 0
res_2 = []
for x in range(N):
    for y in range(N):
        if arr[x][y] and visited[x][y] == 0:
            cnt = 1
            Q = []
            Q.append((x,y))
            visited[x][y] = 1
            while Q:
                cx, cy = Q.pop(0)
                for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
                    nx = cx + dx
                    ny = cy + dy
                    if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and arr[nx][ny]:
                        Q.append((nx, ny))
                        visited[nx][ny] = 1
                        cnt += 1
            if cnt:
                res_1 += 1
                res_2.append(cnt)
res_2.sort()
print(res_1)
for i in res_2:
    print(i)