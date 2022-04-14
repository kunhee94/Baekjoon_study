import sys
sys.stdin = open("input.txt", "r")


def DFS(li):
    if len(li) > M:
        return
    if len(li) == M:
        print(*li)
        return
    for i in arr:
        if li == []:
            DFS(li+[i])
        elif arr and li[-1] <= i:
            DFS(li+[i])


N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
DFS([])