import sys
sys.stdin =open("input.txt", "r")

# N = int(input())
# # 만들어야하는 수열
# target = []
# # 스택
# stack = []
# # 만든 수열
# result = []
# # 출력할것
# final = []
# for i in range(N):
#     num = int(input())
#     target.append(num)
#     for j in range(1, N+1):
#         if num >= j and j not in stack and j not in result:
#             stack.append(j)
#             final.append('+')
#         elif target[i] < j:
#             result.append(stack.pop())
#             final.append('-')
#             break
# while stack != []:
#     result.append(stack.pop())
#     final.append('-')
#
# if result == target:
#     print("\n".join(final))
# else:
#     print('NO')
#


N = int(input())
# 만들어야하는 수열
target = []
# 스택
stack = []
# 만든 수열
result = []
# 출력할것
final = []
for i in range(N):
    num = int(input())
    target.append(num)
    for j in range(1, N+1):
        if num >= j and j not in stack and j not in result:
            stack.append(j)
            final.append('+')
        elif target[i] < j:
            result.append(stack.pop())
            final.append('-')
            break
while stack != []:
    result.append(stack.pop())
    final.append('-')

if result == target:
    print("\n".join(final))
else:
    print('NO')

