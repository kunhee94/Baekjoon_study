import sys
from collections import deque
sys.setrecursionlimit(4000)
sys.stdin =open("input.txt", "r")

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# def DFS(sx, sy, cnt):
#     global res, lis
#     for k in range(4):
#         origin = lis[:]
#         nx = sx + dx[k]
#         ny = sy + dy[k]
#         # 처음보는 알파벳이면
#         if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] not in lis:
#             # 알파벳 수집
#             lis = [*lis,arr[nx][ny]]
#             DFS(nx,ny,cnt+1)
#             lis = origin
#         elif res < cnt:
#             res = cnt
#             return
#
# def BFS(sx, sy):
#     global res
#     Q = deque()
#     Q.append((sx, sy, arr[sx][sy]))
#     while Q:
#         cx, cy, lis = Q.popleft()
#         for k in range(4):
#             nx = cx + dx[k]
#             ny = cy + dy[k]
#             # 처음보는 알파벳이면
#             if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] not in lis:
#                 Q.append((nx, ny, lis + arr[nx][ny]))
#                 res = max(res, len(lis)+1)
#
# N, M = map(int, sys.stdin.readline().rstrip().split())
# arr = [sys.stdin.readline().rstrip() for _ in range(N)]
# lis = [arr[0][0]]
# res = 0
# # DFS(0,0,0)
# # print(res+1)
# # BFS로 풀기
# BFS(0,0)
# print(res)

import sys

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(sx, sy, cnt, trace):
    global res
    res = max(res,cnt)
    for k in range(4):
        nx = sx + dx[k]
        ny = sy + dy[k]
        # 처음보는 알파벳이면
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] not in trace:
            # 알파벳 수집
            DFS(nx, ny, cnt + 1, trace + arr[nx][ny])

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
res = 0
DFS(0, 0, 0, arr[0][0])
print(res + 1)
