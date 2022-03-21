import sys
sys.stdin =open("input.txt", "r")

def BFS(sx, sy):
    Q = []
    # visited[sx][sy] = 1
    # 상하 좌우와 자기 자신까지 체크해야 혼자 떨어진 배추도 체크가능
    # 델타이동 상하 좌우 중앙
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    Q.append([sx, sy])
    # 지렁이 추가했는지 확인
    s = 0
    while Q:
        [cx, cy] = Q.pop(0)
        for k in range(5):
            nx = cx + dx[k]
            ny = cy + dy[k]
            # 인덱스 범위 안이고 배추가 있고 지렁이가 없다면
            if 0 <= nx <N and 0 <= ny < M and arr[nx][ny] and visited[nx][ny] == 0:
                Q.append([nx, ny])
                visited[nx][ny] = 1
                s = 1
    return s
T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    # 밭
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1
    # 지렁이 영역 체크
    visited = [[0]*M for _ in range(N)]
    # 지렁이 수
    res = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] and BFS(x, y):
                res += 1
    print(res)








