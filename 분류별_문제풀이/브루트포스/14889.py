import sys
sys.stdin = open("input.txt", "r")


def DFS(n,cnt):
    global res
    if cnt == N//2:
        start, link = 0,0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    start += (arr[i][j] + arr[j][i])
                elif visited[i] == 0 and visited[j] == 0:
                    link += (arr[i][j] + arr[j][i])
        res = min(res, abs(start-link))

    for i in range(n,N):
        if visited[i] == 0:
            visited[i] = 1
            DFS(i+1,cnt+1)
            visited[i] = 0


N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
res = 99999
visited = [0]*N
DFS(0,0)
print(res)