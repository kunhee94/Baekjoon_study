import sys
sys.stdin = open('input.txt','r')


n = int(input())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(1, len(arr)):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
print(min(arr[n - 1]))