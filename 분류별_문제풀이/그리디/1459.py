from collections import deque
import sys
sys.stdin = open("input.txt", "r")



X, Y, W, S = map(int, input().split())
x,y = 0,0
res = 0
if W*2 < S:
    res = (X+Y)*W
else:
    if W > S:
        if X == Y:
            res = S*X
        elif X > Y:
            # 홓수일 때
            if X % 2:
                res = Y*S + (X-Y-1)*S + W
            # 짝수일 때
            else:
                res = Y * S + (X - Y) * S
        else:
            # 홀수일 때
            if Y % 2:
                res = X * S + (Y - X - 1) * S + W
            # 짝수 일 때
            else:
                res = X*S + (Y-X-1)*S + W
    else:
        if X > Y:
            res += Y * S
            x, y = Y, Y
        else:
            res += X * S
            x, y = X, X
        res += ((X - x) + (Y - y)) * W
print(res)







# X, Y, W, S = map(int, input().split())
#
#
# # 우,하,우하
# dx = [0,1,1]
# dy = [1,0,1]
#
#
# visited = [[99999]*(X+1) for _ in range(Y+1)]
# Q = deque()
# Q.append((0, 0))
# visited[0][0] = 0
# res = 0
# while Q:
#     cx,cy = Q.popleft()
#     if cx == Y and cy == X:
#         res = visited[cx][cy]
#         break
#     for k in range(3):
#         nx = cx + dx[k]
#         ny = cy + dy[k]
#         if nx < Y+1 and ny < X+1 and visited[nx][ny] > visited[cx][cy]:
#             if k != 2:
#                 visited[nx][ny] = visited[cx][cy] + W
#             else:
#                 visited[nx][ny] = visited[cx][cy] + S
#             Q.append((nx,ny))
#
# print(res)



