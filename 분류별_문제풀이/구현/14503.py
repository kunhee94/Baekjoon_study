import sys
sys.stdin = open('input.txt','r')

# 상우하좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]
# opp
opp = [3,0,1,2]


N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0
while True:
    # 현재 칸 청소
    if not visited[x][y]:
        visited[x][y] = 1
        cnt += 1
    temp = 0
    # 만약 현재 기준왼쪽에 청소한적 없는 빈칸이 있으면 이동, 이걸 4방향 체크
    for k in range(4):
        nx = x + dx[opp[d]]
        ny = y + dy[opp[d]]
        d = opp[d]
        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny] and not visited[nx][ny]:
            x, y = nx, ny
            temp = 1
            break
    # 이동에 성공했으면 다시 while문
    if temp:
        continue
    # 4방향 확인 후 이동 실패 했고 뒤쪽이 벽이면 작동 정지
    else:
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny]:
            break
        # 벽이 아니면 한칸 후진
        else:
            x, y = nx, ny
            continue
print(cnt)



