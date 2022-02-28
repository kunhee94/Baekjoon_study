import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
K = int(input())
# 출력할 때는 결과에 +1씩해서 출력해야한다.
arr = [[0]*M for _ in range(N)]
# 우하좌상 이동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0
x, y = 0, 0

if K <= N * M:
    for i in range(1, K+1):
        arr[x][y] = i
        x = x + dx[cnt]
        y = y + dy[cnt]
        if 0 > x or x > N-1 or 0 > y or y > M-1 or arr[x][y] != 0:
            x = x - dx[cnt]
            y = y - dy[cnt]
            cnt = (cnt+1) % 4
            x = x + dx[cnt]
            y = y + dy[cnt]

    print(x-dx[cnt] + 1, y-dy[cnt] + 1)
else:
    print(0)




