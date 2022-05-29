import sys
sys.stdin = open("input.txt","r")



def DFS(cnt, s):
    global res
    if cnt == N-1:
        res += 1
        return
    s -= K
    for i in range(len(arr)):
        if not visited[i]:
            if s+arr[i] >= 500:
                visited[i] = 1
                DFS(cnt+1, s+arr[i])
                visited[i] = 0


N, K = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0]*N
res = 0
DFS(0, 500)
print(res)