T = int(input())
numbers = []
for tc in range(T):
    num = int(input())
    numbers.append(num)
numbers.sort()
for j in range(len(numbers)):
    print(numbers[j])
# 내장함수를 써도 속도에서 오류남 퀵정렬을 배우고 다시 해보자
# 2번 풀이
import sys
T = int(sys.stdin.readline())
numbers = []
for tc in range(T):
    num = int(sys.stdin.readline())
    numbers.append(num)
numbers.sort()
for j in range(len(numbers)):
    print(numbers[j])
# input()을 sys.stdin.readiline()으로 바꾸니까 해결됨