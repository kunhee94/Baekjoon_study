import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
plan = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plan.sort(key= lambda x:(x[1], x[0]))
cnt = 1
time = plan[0][1]
print(plan)
# 현재 종료시간보다 시작시간이 크거나 같은거 중에서 젤빨리 시작하는거
for i in range(1, len(plan)):
    if plan[i][0] >= time:
        time = plan[i][1]
        cnt += 1
print(cnt)




