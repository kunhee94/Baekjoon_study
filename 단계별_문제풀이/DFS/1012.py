import sys
sys.stdin =open("input.txt", "r")
#
# T = int(input())
#
# for tc in range(T):
#     M, N, K = map(int, input().split())
#     arr = [[0]*M for _ in range(N)]
#     # 지렁이 체크
#     visited = [[0]*M for _ in range(N)]
#     # 결과
#     cnt = 0
#     # 델타 검색 상우하좌
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     for _ in range(K):
#         c, r = map(int, input().split())
#         arr[r][c] = 1
#     for x in range(N):
#         for y in range(M):
#             # 배추가 존재하고 활동하는 지렁이 없을때만 체크
#             if arr[x][y] and visited[x][y] == 0:
#                 worm = 0
#                 for p in range(4):
#                     nx = x + dx[p]
#                     ny = y + dy[p]
#                     # 사방에도 지렁이 없는지 체크
#                     if 0 <= nx < N and 0 <= ny < M:
#                         if visited[nx][ny]:
#                             worm += 1
#                 # 사방에도 지렁이 없으면 지렁이 놓고
#                 if worm == 0:
#                     cnt += 1
#                     # 자기 포함 사방으로 지렁이 영역표시
#                     visited[x][y] = 1
#                     for p in range(4):
#                         nx = x + dx[p]
#                         ny = y + dy[p]
#                         if 0 <= nx < N and 0 <= ny < M:
#                             visited[nx][ny] = 1
#                 # 사방 중 한곳에라도 지렁이 있으면 다시 자기포함 4방에 지렁이 영역표시만 함
#                 else:
#                     visited[x][y] = 1
#                     for p in range(4):
#                         nx = x + dx[p]
#                         ny = y + dy[p]
#                         if 0 <= nx < N and 0 <= ny < M:
#                             visited[nx][ny] = 1
#             # 배추가 있는데 지렁이 활동 구역이면 다시 사방에 지렁이 영역표시
#             elif arr[x][y] and visited[x][y]:
#                 for p in range(4):
#                     nx = x + dx[p]
#                     ny = y + dy[p]
#                     if 0 <= nx < N and 0 <= ny < M:
#                         visited[nx][ny] = 1
#     print(cnt)


T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    # 밭
    arr = [[0]*M for _ in range(N)]
    # 지렁이 영역 체크
    visited = [[0]*M for _ in range(N)]
    # 지렁이 수
    cnt = 0
    # 델타 검색 상우하좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for _ in range(K):
        c, r = map(int, input().split())
        arr[r][c] = 1
    for x in range(N):
        for y in range(M):
            # 배추가 존재할때
            if arr[x][y] and visited[x][y] == 0:
                # 연결된 배추가 있고 그 배추에 활동하는 지렁이 있는지 체크
                worm = 0
                for p in range(4):
                    nx = x + dx[p]
                    ny = y + dy[p]
                    if 0 <= nx < N and 0 <= ny < M:
                        if arr[nx][ny] and visited[nx][ny]:
                            worm += 1
                # 사방에 배추와 연결된 지렁영역 없으면 지렁이 추가
                if worm == 0:
                    cnt += 1
                    # 자기 포함 사방으로 지렁이 영역표시
                    visited[x][y] = 1
                    for p in range(4):
                        nx = x + dx[p]
                        ny = y + dy[p]
                        if 0 <= nx < N and 0 <= ny < M:
                            visited[nx][ny] = 1
                # 배추와 연결된 지렁이가 있다면 자기 포함 사방에 지렁영역 표시
                else:
                    visited[x][y] = 1
                    for p in range(4):
                        nx = x + dx[p]
                        ny = y + dy[p]
                        if 0 <= nx < N and 0 <= ny < M:
                            visited[nx][ny] = 1
            # 배추가 있는데 지렁이 활동 구역이면 사방에 지렁이 영역표시
            elif arr[x][y] and visited[x][y]:
                for p in range(4):
                    nx = x + dx[p]
                    ny = y + dy[p]
                    if 0 <= nx < N and 0 <= ny < M:
                        visited[nx][ny] = 1
    print(cnt)






