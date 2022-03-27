import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T = int(input())

# 나이트 이동
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]
