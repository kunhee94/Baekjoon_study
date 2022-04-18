import sys
sys.stdin = open("input.txt", "r")


N = int(input())
res = set()
for i in range(N):
    a = sys.stdin.readline().rstrip()
    res.add(a)
res = list(res)
res.sort()
res.sort(key=lambda x:len(x))
for i in res:
    print(i)



