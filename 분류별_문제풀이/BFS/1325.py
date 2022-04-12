import sys
from collections import deque
sys.stdin =open("input.txt", "r")

def BFS(sy,cnt):
    Q = deque()
    Q.append(sy)
    res = cnt
    while Q:
        cy = Q.popleft()
        for k in range(1, N+1):
            if arr[cy][k]:
                res += 1
                Q.append(k)
    return res

N, M = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    arr[x][y] = 1

count = 0
result = []
for x in range(1, N+1):
    for y in range(1, N+1):
        if arr[x][y]:
            A = BFS(y,1)
            result.append([x,A])
result.sort(key=lambda x:x[1], reverse=True)
for i in result:
    if i[1] == result[0][1]:
        print(i[0], end=' ')


