import sys
sys.stdin = open("input.txt", "r")


def DFS(li):
    if len(li) > M:
        return
    if len(li) == M:
        print(*li)
        return
    for i in arr:
        if li and li[-1] <= i:
            DFS(li+[i])
        elif li == []:
            DFS(li+[i])

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
DFS([])