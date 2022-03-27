import sys
sys.stdin =open("input.txt", "r")
import copy

N, M = map(int, input().split())

arr = [list(map(str, input())) for _ in range(N)]
result = []


