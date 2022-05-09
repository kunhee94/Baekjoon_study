from collections import deque
import sys
sys.stdin = open('input.txt','r')


# 사과를 먹으면 뱀길이 늘어남
# 벽이나 자기지신의 몸과 부딪히면 게임 끝
# 뱀은 0,0 시작 길이는 1 처음엔 오른쪽

# 1.다음칸에 몸길이 늘려서 이동
# 2-1.사과가 있으면 사과 사라지고 꼬리는 그전칸 그대로
# 2-2.사과 없으면 꼬리를 끌고와서 몸길이 그전 그대로 유지

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
# 방향전환 횟수
L = int(input())
L_list = []
for _ in range(L):
    X, C = input().split()
    X = int(X)
    L_list.append([X, C])

arr = [[0]*N for _ in range(N)]

# 사과 표시
for x, y in apples:
    arr[x-1][y-1] = 1

# 우하좌상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 뱀 초기위치, 방향 초기
x, y, d = 0, 0, 0

# 뱀
snake = deque()
time = 0
while True:
    # 뱀머리 현재 위치
    arr[x][y] = 2
    snake.append((x,y))
    for i in range(L):
        # 방향을 틀어야한다면
        if L_list[i][0] == time:
            # 만약 시계방향으로 돈다면
            if L_list[i][1] == 'D':
                d = (d+1) % 4
            else:
                d = (d-1) % 4
    nx = x + dx[d]
    ny = y + dy[d]
    # 벽에 부딪히거나 자기 몸과 부딪히면
    if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] == 2:
        time += 1
        break
    # 벽이 아니면
    elif 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 2:
        # 사과가 없다면
        if not arr[nx][ny]:
            # 꼬리 없애주고
            i, j = snake.popleft()
            arr[i][j] = 0
            # 머리 이동
            x, y = nx, ny
            time += 1
        # 사과라면 꼬리 남기고 머리만 이동
        else:
            x, y = nx, ny
            time += 1

print(time)