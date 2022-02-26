import sys
sys.stdin = open("input.txt", "r")
K = int(input())
lengh = []
for i in range(6):
    P, L = map(int, input().split())
    lengh.append(L)
rectangle = []
small = 0
for i in range(1, 6):
    rectangle.append(lengh[i]*lengh[i-1])
# 이케이스는 for문 돌때 안들어가서 오답났었음
rectangle.append(lengh[0]*lengh[5])
for i in range(6):
    if rectangle[i] == max(rectangle):
        # 제일 큰 사각형 찾고 3번쨰 뒤의 사각형이 잘라내야할 사각형
        small = rectangle[(i+3) % 6]
print((max(rectangle)-small)*K)
