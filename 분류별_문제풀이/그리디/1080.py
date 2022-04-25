import sys
sys.stdin = open("input.txt", "r")

def swap(sx,sy):
    for x in range(sx, sx+3):
        for y in range(sy, sy+3):
            if A[x][y]:
                A[x][y] = 0
            else:
                A[x][y] = 1


N, M = map(int, input().split())

A = [list(map(int, input()))for _ in range(N)]
B = [list(map(int, input()))for _ in range(N)]
cnt = 0
for x in range(N-2):
    for y in range(M-2):
        if A[x][y] != B[x][y]:
            swap(x,y)
            cnt += 1
if A == B:
    print(cnt)
else:
    print(-1)




