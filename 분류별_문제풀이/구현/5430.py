from collections import deque
import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    try:
        arr = deque(map(int,sys.stdin.readline().rstrip().strip('[]').split(',')))
        i = 0
        temp = 1
        while i < len(p):
            # 뒤집기 함수
            if p[i] == 'R':
                arr.reverse()
            # 맨 앞 빼기 함수
            else:
                arr.popleft()
            # 빈배열이 되었다면
            if not arr:
                print('error')
                temp = 0
                break
            i += 1
        if temp:
            print(list(arr))
    except:
        print('error')




















# T = int(input())
# for tc in range(T):
#     p = input()
#     n = int(input())
#     try:
#         arr = list(map(int,sys.stdin.readline().rstrip().strip('[]').split(',')))
#         i = 0
#         temp = 1
#         while i < len(p):
#             # 뒤집기 함수
#             if p[i] == 'R':
#                 arr.reverse()
#             # 맨 앞 빼기 함수
#             else:
#                 arr = arr[1:]
#             # 빈배열이 되었다면
#             if not arr:
#                 print('error')
#                 temp = 0
#                 break
#             i += 1
#         if temp:
#             print(arr)
#     except:
#         print('error')

