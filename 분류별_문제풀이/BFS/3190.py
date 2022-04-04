import sys
from collections import deque
sys.stdin = open("input.txt", "r")








N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
apple = [list(map(int, sys.stdin.readline().rstrip().split()))for _ in range(K)]
C = int(sys.stdin.readline().rstrip())
move = [list(map(int, sys.stdin.readline().rstrip().split()))for _ in range(C)]
arr = [[0]*N for _ in range(N)]
for i in apple:
    # 사과 위치 표시
    arr[i[0]][i[1]] = 1
DFS(0,0,1)