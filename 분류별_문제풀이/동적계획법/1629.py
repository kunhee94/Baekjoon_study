import sys
sys.stdin = open('input.txt','r')

A,B,C = map(int, input().split())

arr = [0]*B
arr[0] = A
for i in range(1, len(arr)):
    arr[i] = arr[i-1]*arr[0]

print(arr[B-1] % C)
