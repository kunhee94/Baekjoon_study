import sys
sys.stdin =open("input.txt", "r")
# 문제 제대로 안읽어서 틀림
while True:
    word = input()
    if word == '.':
        break
    stack = []
    for i in word:
        # 여는 괄호면 스택에 추가
        if i == '(' or i == '[':
            stack.append(i)
        # 닫는 괄호면
        elif i == ')':
            # 스택이 비워져있지 않고 top이 매치되는 여는 괄호면 pop
            if stack and stack[-1] == '(':
                stack.pop()
            # 스택이 비워져있거나  top과 매치가 안되면 no
            else:
                print('no')
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break
    # for문이 정상 종료 되었는데 스택이 비워져있지 않으면 no
    else:
        if stack:
            print('no')
        else:
            print('yes')
