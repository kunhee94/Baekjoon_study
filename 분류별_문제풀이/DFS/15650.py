import sys
sys.stdin = open("input.txt", "r")


def DFS(li):
    if len(li) > M:
        return
    if len(li) == M:
        print(*li)
        return
    for i in arr:
        # 중복아니고 항상 오름차순으로
        if i not in li:
                if li and li[-1] < i:
                    DFS(li+[i])
                elif li == []:
                    DFS(li+[i])

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
DFS([])