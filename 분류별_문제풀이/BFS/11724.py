import sys
from collections import deque
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())
arr = dict()
for i in range(1, N+1):
    arr[str(i)] = []
for i in range(M):
    s, e = input().split()
    arr[s].append(e)
    arr[e].append(s)
cnt = 0
visited = [0]*(N+1)
Q = deque()
for i in range(1, N+1):
    # 방문한적 없으면 cnt 증가시켜주고
    # BFS 돌려서 현위치에서 갈수 있는곳 전부 가면서 방문표시
    if visited[i] == 0:
        cnt += 1
        visited[i] = 1
        Q.append(str(i))
        while Q:
            now = Q.popleft()
            if arr[now]:
                for j in arr[now]:
                    if visited[int(j)] == 0:
                        Q.append(j)
                        visited[int(j)] = 1
print(cnt)









