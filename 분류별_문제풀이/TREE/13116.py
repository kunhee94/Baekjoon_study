import sys
sys.stdin = open("input.txt", "r")




def find_anc(n):
    if n:
        result.add(n)
        find_anc(n//2)


T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    result = set()
    find_anc(A)
    a = result
    result = set()
    find_anc(B)
    b = result
    print(max(a & b) * 10)




