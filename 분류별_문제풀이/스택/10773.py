import sys
sys.stdin =open("input.txt", "r")

K = int(input())
stack = []
for _ in range(K):
    N = int(input())
    #  N이 0이 아니면
    if N:
        stack.append(N)
    else:
        stack.pop()
print(sum(stack))