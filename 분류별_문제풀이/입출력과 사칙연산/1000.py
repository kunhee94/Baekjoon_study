# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
a=list(map(int,input().split()))
# .split():공백을 기준으로 문자열을 나누어 줌
# map(int,list()): 공백을 기준으로 입력받은 각각의 원소를 int형으로 변환시켜 list에 할당한다.
total=0
for i in a:
    total=total+i
print(total)