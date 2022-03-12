import sys
sys.stdin = open("input.txt", "r")
#  왜 시간초과가 나지?
T = int(input())
stack = []

for tc in range(T):
    order = input()
    # push 일 경우
    if order[0:4] == "push":
        stack.append(int(order[5:]))
    # pop일 경우 비어있으면 -1 출력 아니면 스택의 top을 pop
    elif order == "pop":
        # 안비었으면 pop
        if stack:
            print(stack.pop())
        else:
            print(-1)
    # size인 경우
    elif order == "size":
        print(len(stack))
    # empty
    elif order == "empty":
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)