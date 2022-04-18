import sys
sys.stdin = open("input.txt", "r")


def make_P(n):
    res = ''
    for i in range((2*n)+1):
        # 홀수면 o
        if i%2:
            res += 'O'
        else:
            res += 'I'
    return res


N = int(input())
M = int(input())
word = sys.stdin.readline().rstrip()
pn = make_P(N)
res = 0
for i in range(0, M - ((2*N)-1)):
    if word[i:i+len(pn)] == pn:
        res += 1
print(res)

