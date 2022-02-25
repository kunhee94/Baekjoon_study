import sys
sys.stdin =open("input.txt", "r")
import copy

# N, M = map(int, input().split())
#
# arr = [input() for _ in range(N)]
#
# a = arr[::]
# result = []
# for x in range(N-8+1):
#     for y in range(M-8+1):
#         # 8*8확인
#         cnt =0
#         for k in range(x, x+8):
#             cnt_s = 0
#             for p in range(y+1, y+8):
#                 if a[k][p] == a[k][p-1]:
#                     # if a[k][p] == 'B':
#                     #     a[k][p] = 'W'
#                     # else:
#                     #     a[k][p] = 'B'
#                     cnt_s += 1
#             cnt += cnt_s
#         result.append(cnt)
#
# print(min(result))




N, M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]


result = []

for x in range(N-8+1):
    for y in range(M-8+1):
        # 8*8확인
        cnt =0
        for k in range(x, x+8):
            cnt_s = 0
            a = copy.deepcopy(arr)
            for p in range(y+1, y+8):
                if a[k][p] == a[k][p-1]:
                    if a[k][p] == 'B':
                        a[k][p] = 'W'
                    else:
                        a[k][p] = 'B'
                    cnt_s += 1
            cnt += cnt_s
        result.append(cnt)


print(result)

