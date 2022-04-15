import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def BFS(start,target,s):
    Q = deque()
    Q.append((start,target,s))
    visited = [[0] * (V + 1) for _ in range(V + 1)]
    while Q:
        now, end, ssum = Q.popleft()
        if now == end:
            print(ssum)
            return
        for i in range(1, V+1):
            if arr[now][i] and visited[now][i] == 0:
                visited[now][i] = 1
                Q.append((i, end, ssum + arr[now][i]))
    print('INF')
    return

V, E = map(int, input().split())
K = int(input())
arr = [[0]*(V+1) for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    arr[u][v] = w

for i in range(1,V+1):
    BFS(K, i,0)
