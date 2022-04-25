import sys
sys.stdin = open("input.txt", "r")





T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.sort()
    res = 0
    for i in range(2, N):
        res = max(res, abs(arr[i]-arr[i-2]))
    print(res)