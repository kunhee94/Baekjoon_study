import sys
sys.stdin = open("input.txt", "r")

def DFS(s):
    global cnt
    if s > n:
        return
    if s == n:
        cnt += 1
        return
    DFS(s+1)
    DFS(s+2)
    DFS(s+3)

T = int(input())

for tc in range(T):
    n = int(input())
    cnt = 0
    DFS(0)
    print(cnt)