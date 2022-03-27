import sys

T = int(sys.stdin.readline().rstrip())
stack = [0]*10001
top = -1
for tc in range(T):
    order = sys.stdin.readline().rstrip()
    # pop일 경우 비어있으면 -1 출력 아니면 스택의 top을 pop
    if order == "pop":
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    # size인 경우
    elif order == "size":
        print(top + 1)
    # empty
    elif order == "empty":
        if top == -1:
            print(1)
        else:
            print(0)
    elif order == "top":
        if top == -1:
            print(-1)
        else:
            print(stack[top])
    # push 일 경우
    else:
        top += 1
        stack[top] = order[5:]

