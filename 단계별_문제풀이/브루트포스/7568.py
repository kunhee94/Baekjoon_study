
N = int(input())

people = [list(map(int, input().split())) for _ in range(N)]
result = [0]*N
for k in range(N):
    bigger_man = 0
    for i in range(N):
        if people[k][0] < people[i][0] and people[k][1] < people[i][1]:
            bigger_man += 1
    result[k] = bigger_man + 1
print(*result)