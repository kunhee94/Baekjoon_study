from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def BFS(sx,sy):
    global res
    for word in ('B','W'):
        visited = [[0] * M for _ in range(N)]
        Q = deque()
        Q.append((sx,sy))
        cnt = 0
        if arr[sx][sy] != word:
            cnt = 1
        visited[sx][sy] = word
        while Q:
            cx,cy = Q.popleft()
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                if sx <= nx < sx+8 and sy <= ny < sy+8 and visited[nx][ny] == 0:
                   if visited[cx][cy] == arr[nx][ny]:
                       if visited[cx][cy] == 'B':
                           visited[nx][ny] = 'W'
                           cnt += 1
                       else:
                           visited[nx][ny] = 'B'
                           cnt += 1
                   else:
                       visited[nx][ny] = arr[nx][ny]
                   Q.append((nx,ny))
        if res > cnt:
            res = cnt

N, M = map(int, input().split())
arr = list(input()for _ in range(N))
res = 999999
for x in range(N-7):
    for y in range(M-7):
        BFS(x,y)

print(res)
