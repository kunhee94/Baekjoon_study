import sys

sys.stdin = open("input.txt", "r")


N, M = map(int, sys.stdin.readline().rstrip().split())
cant_see = set()
cant_hear = set()
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    cant_see.add(word)
for _ in range(M):
    word = sys.stdin.readline().rstrip()
    cant_hear.add(word)
res = []
for i in cant_see:
    if i in cant_hear:
        res.append(i)
res.sort()
print(len(res))
for i in res:
    print(i)


