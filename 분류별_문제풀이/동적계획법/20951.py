import sys
sys.stdin = open("input.txt", "r")


N, M = map(int, sys.stdin.readline().split())
arr = [[0]*(N+1) for _ in range(N+1)]
