import sys
res = ''
a = sorted(sys.stdin.readline().rstrip(),reverse=True)
for i in a:
    res += i
print(res)



