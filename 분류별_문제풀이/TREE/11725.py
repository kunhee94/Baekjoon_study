import sys
from collections import deque
sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")

def DFS(n):
    if 0 not in visited[2:]:
        return
    for i in arr[n]:
        if visited[i] == 0:
            visited[i] = n
            DFS(i)


N = int(input())

arr = [[] for _ in range(N+1)]
for i in range(N-1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [0]*(N+1)

# DFS(1)
Q = deque()
Q.append(1)
while Q:
    now = Q.popleft()
    for i in arr[now]:
        if visited[i] == 0:
            visited[i] = now
            Q.append(i)
for i in visited[2:]:
    print(i)
