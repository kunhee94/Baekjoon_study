import sys
sys.stdin = open("input.txt", "r")


a, b, c = map(int, input())

def cal(num, N):
    global c
    if N == 1:
        return num % c
    else:


