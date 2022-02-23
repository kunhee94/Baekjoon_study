import sys
sys.stdin = open("input.txt", "r")

M, N = map(int, input().split())

T = int(input())

arr = [[0]*M for _ in range(N)]

for _ in range(T):
    P, K = map(int, input().split())
    # 가로로 나눌 때 K 기준으로 위는 111더해주고 아래는 222 더해준다(절대 겹치는거 없게 하기위해)
    if P == 0:
        for x in range(K):
            for y in range(M):
                arr[x][y] += 111
        for x in range(K, N):
            for y in range(M):
                arr[x][y] += 222
    # 세로로 나눌 때 K 기준 좌로는 10 우로는 20 더해준다
    else:
        for y in range(K):
            for x in range(N):
                arr[x][y] += 10
        for y in range(K, M):
            for x in range(N):
                arr[x][y] += 20

# 작업이 끝났다면 arr안의 숫자 종류별로 모아본다
what_number = set()
for x in range(N):
    for y in range(M):
        what_number.add(arr[x][y])
# what_number의 각 수가 몇개씩 들어있는지 센다.
what_number = list(what_number)

result = [0]*len(what_number)

for i in range(len(what_number)):
    for x in range(N):
        for y in range(M):
            if what_number[i] == arr[x][y]:
                result[i] += 1
# 제일 많이나온 갯수 출력하면됨
print(max(result))








