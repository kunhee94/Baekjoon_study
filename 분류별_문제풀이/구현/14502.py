from collections import deque
import sys
sys.stdin = open('input.txt','r')


# 벽을 세울수 있는 리스트 만들기
# 그중에 3개를 뽑아서 벽으로 만들기
# 벽으로 만들었으면 그거 BFS 돌려서 안전영역 구하기
# 결과값과 비교해서 최댓값 찾기

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def BFS(lli):
    global safe,res
    for x,y in lli:
        arr[x][y] = 1
    Q = deque()
    visited = [[0]*M for _ in range(N)]
    for x,y in birus:
        visited[x][y] = 1
        Q.append((x,y))
    cnt = 0
    while Q:
        cx,cy = Q.popleft()
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not arr[nx][ny]:
                visited[nx][ny] = 1
                Q.append((nx,ny))
                cnt += 1
    # 최초 빈칸의 수 -3 -바이러스가 퍼진 수 = 안전공간
    cnt = safe - cnt - 3
    if res < cnt:
        res = cnt
    # 벽 다시 원상복구
    for x,y in lli:
        arr[x][y] = 0



def DFS(n,li):
    if len(li) == 3:
        BFS(li)
        return
    for i in range(n, len(spaces)):
        DFS(i+1, [*li,spaces[i]])



N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 벽을 세울수 있는 곳
spaces = []
birus = []
for x in range(N):
    for y in range(M):
        if not arr[x][y]:
            spaces.append([x,y])
        elif arr[x][y] == 2:
            birus.append([x,y])
safe = len(spaces)
res = 0
DFS(0,[])
print(res)


