import sys
sys.stdin = open("input.txt", "r")
# 시간초과 발생
# def fibo(N):
#     global cnt_1
#     global cnt_0
#     if N == 1:
#         cnt_1 += 1
#         return N
#     elif N == 0:
#         cnt_0 += 1
#         return N
#     else:
#         return fibo(N-1) + fibo(N-2)
#
#
# T = int(input())
#
# for tc in range(1, 1+T):
#     K = int(input())
#     cnt_0 = 0
#     cnt_1 = 0
#     fibo(K)
#     print(cnt_0, cnt_1, end=' ')
#     print()


T = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]
def fibo_cnt(N):
    # 뒤에부터 N까지 집어넣어야한다.
    while len(zero) <= N:
        for i in range(len(zero), N+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[N], one[N])


for tc in range(1, 1+T):
    K = int(input())
    fibo_cnt(K)
