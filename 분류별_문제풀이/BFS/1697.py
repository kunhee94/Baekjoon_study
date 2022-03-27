import sys
sys.stdin = open("input.txt", "r")
def DFS(now, target, time):
    global ans
    if now == target:
        if ans > time:
            ans = time
        return
    if now > target:
        if now > 2*target:
            return
        else:
            DFS(now - 1, target, time + 1)
    else:
        DFS(now+1, target, time+1)
        DFS(now*2, target, time+1)
N, K = map(int, input().split())
ans = 99999999
DFS(N, K, 0)
print(ans)

