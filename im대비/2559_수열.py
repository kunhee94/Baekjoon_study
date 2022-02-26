import sys
sys.stdin = open("input.txt", "r")

# # 시간초과 떳음
N, K = map(int, input().split())

arr = list(map(int, input().split()))

result = -400

for i in range(N-K+1):
    if sum(arr[i:i+K]) > result:
        result = sum(arr[i:i+K])

print(result)


# 앞에거 빼고 뒤에거 더하는식으로하니까 시간초과 발생 x
N, K = map(int, input().split())

arr = list(map(int, input().split()))


result = [sum(arr[0:K])]

start = sum(arr[0:K])

for i in range(N-K):
    start = start - arr[i] + arr[i+K]
    result.append(start)

print(max(result))