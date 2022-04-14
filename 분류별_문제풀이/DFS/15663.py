import sys
sys.stdin = open("input.txt", "r")

# 문자열은 정렬할때 앞에서부터 비교하면서 정렬함

def DFS(li, cnt):
    if cnt == M:
        res.add(li)
        return
    for i in range(len(arr)):
        if visited[i] == 0:
            visited[i] = 1
            DFS(li + ' ' + str(arr[i]), cnt + 1)
            visited[i] = 0

N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
res = set()
visited = [0]*N
DFS('', 0)
res = list(res)
final = []
for i in res:
    a = i[1:].split(' ')
    final.append(list(map(int,a)))
final.sort()
for i in final:
    print(*i)

