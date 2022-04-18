import sys
sys.stdin = open("input.txt", "r")


def DFS(n, s):
    global res
    if n == N+1:
        res.append(s)
        return
    for i in range(n, N+1):
        if i+T[i] <= N+1:
            DFS(i+T[i], s+P[i])
        else:
            res.append(s)



N = int(input())
T = [0]
P = [0]
for _ in range(N):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    T.append(t)
    P.append(p)
res = []

DFS(1, 0)
print(max(res))