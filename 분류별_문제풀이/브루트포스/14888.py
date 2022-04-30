import sys
sys.stdin = open("input.txt", "r")


def DFS(s,cnt,n):
    global res_max,res_min
    if s > 1000000000:
        return
    if s < -1000000000:
        return

    if cnt == len(arr)-1:
        if s > res_max:
            res_max = s
        if s < res_min:
            res_min = s
        return
    for i in range(4):
        if visited[i] < cals[i]:
            visited[i] += 1
            if i == 0:
                DFS(s+arr[n+1], cnt+1, n+1)
                visited[i] -= 1
            if i == 1:
                DFS(s - arr[n + 1], cnt + 1, n + 1)
                visited[i] -= 1
            if i == 2:
                DFS(s * arr[n + 1], cnt + 1, n + 1)
                visited[i] -= 1
            if i == 3:
                # 음수일때
                if s < 0:
                    s = -((-s)//arr[n+1])
                    DFS(s, cnt + 1, n + 1)
                else:
                    DFS(s // arr[n + 1], cnt + 1, n + 1)
                visited[i] -= 1

N = int(input())
arr = list(map(int, input().split()))
# +,-,*,/
cals = list(map(int, input().split()))
visited = [0]*len(cals)
res_max = -999999999999999
res_min = 99999999999999
DFS(arr[0], 0, 0)
print(res_max)
print(res_min)


