import sys
sys.stdin = open('input.txt', 'r')


def check_dt(llis):
    global res
    how_long = 0
    for home in house:
        chi_dt = 999
        # 각 집에서 제일 가까운 치킨거리를 찾기
        for j in range(M):
            chi_dt = min(chi_dt, abs(home[0]-llis[j][0]) + abs(home[1]-llis[j][1]))
        # 도시의 치킨거리에 누적해주기
        how_long += chi_dt
    # 지금까지의 치킨거리보다 더 좋은 경우가 나왔으면 결과값 체인지
    res = min(res,how_long)

def DFS(n, li):
    if len(li) == M:
        check_dt(li)
        return
    for i in range(n, len(chik)):
        DFS(i+1, li+[chik[i]])

N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
house = []
chik = []
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            house.append([x,y])
        elif arr[x][y] == 2:
            chik.append([x,y])

res = 999999999
DFS(0,[])
print(res)