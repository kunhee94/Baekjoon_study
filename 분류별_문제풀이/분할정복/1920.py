import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())
nums_1 = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
nums_2 = list(map(int, sys.stdin.readline().rstrip().split()))
for i in nums_2:
    if i in nums_1:
        print(1)
    else:
        print(0)