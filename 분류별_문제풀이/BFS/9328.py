import sys
from collections import deque
sys.stdin = open("input.txt", "r")



# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
#
#
#
# def BFS(sx,sy):
#     global keys
#     cnt = 0
#     visited = [[0] * M for _ in range(N)]
#     Q = deque()
#     Q.append((sx,sy))
#     visited[sx][sy] = 1
#     while Q:
#         cx, cy = Q.popleft()
#         # 문서면 cnt 추가하고 바꿔주기
#         if arr[cx][cy] == '$':
#             cnt += 1
#             arr[cx][cy] = '.'
#         # 키면 키추가
#         if arr[cx][cy].islower():
#             keys.add(arr[cx][cy].upper())
#         if arr[cx][cy].isupper() and arr[cx][cy] not in keys:
#             continue
#         for k in range(4):
#             nx = cx + dx[k]
#             ny = cy + dy[k]
#             # 인덱스 범위 안이고 방문안했으면
#             if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
#                 # 빈공간이거나 가지고 있는 키의 문이거나 문서거나 키면 BFS
#                 if arr[nx][ny] == '.' or arr[nx][ny] in keys or arr[nx][ny] == '$' or arr[nx][ny].islower():
#                     Q.append((nx,ny))
#                     visited[nx][ny] = 1
#     return cnt
#
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     arr = [list(sys.stdin.readline().rstrip())for _ in range(N)]
#     K = input()
#     keys = set()
#     if K != '0':
#         keys = set(K.upper())
#     res = 0
#     for y in range(M):
#         # 벽아니면 BFS
#         if arr[0][y] != '*':
#             res += BFS(0, y)
#         if arr[N-1][y] != '*':
#             res += BFS(N-1, y)
#     for x in range(N):
#         if arr[x][0] != '*':
#             res += BFS(x, 0)
#         if arr[x][M-1] != '*':
#             res += BFS(x, M-1)
#     print(res)
dx = [0,0,-1,1]
dy = [1,-1,0,0]



def BFS(sx,sy):
    global keys
    cnt = 0
    Q = deque()
    Q.append((sx,sy))
    for _ in range(2):
        visited = [[0] * M for _ in range(N)]
        while Q:
            cx, cy = Q.popleft()
            visited[cx][cy] = 1
            # 문서면 cnt 추가하고 바꿔주기
            if arr[cx][cy] == '$':
                cnt += 1
                arr[cx][cy] = '.'
            # 키면 키추가
            if arr[cx][cy].islower():
                keys.add(arr[cx][cy].upper())
                arr[cx][cy] = '.'
            # 키없는 문이면 못감
            if arr[cx][cy].isupper() and arr[cx][cy] not in keys:
                continue
            for k in range(4):
                nx = cx + dx[k]
                ny = cy + dy[k]
                # 인덱스 범위 안이고 방문안했으면
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                    # 빈공간이거나 가지고 있는 키의 문이거나 문서거나 키면 BFS
                    if arr[nx][ny] == '.' or arr[nx][ny] in keys or arr[nx][ny] == '$' or arr[nx][ny].islower():
                        Q.append((nx,ny))
                        visited[nx][ny] = 1
    return cnt
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(sys.stdin.readline().rstrip())for _ in range(N)]
    K = input()
    keys = set()
    if K != '0':
        keys = set(K.upper())
    for x in range(N):
        for y in range(M):
            if arr[x][y] in keys:
                arr[x][y] = '.'
    res = 0
    for y in range(M):
        # 벽아니면 BFS
        if arr[0][y] != '*':
            res += BFS(0, y)
        if arr[N-1][y] != '*':
            res += BFS(N-1, y)
    for x in range(N):
        if arr[x][0] != '*':
            res += BFS(x, 0)
        if arr[x][M-1] != '*':
            res += BFS(x, M-1)
    print(res)

