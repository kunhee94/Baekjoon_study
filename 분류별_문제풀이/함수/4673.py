

# 파이썬이아니라 pypy3로 제출하니까 통과함

# 각자릿수 더하는 방법 1
def self_number(a):
    # a보다 작은 모든수로 생성자 함수를 넣었는데
    # 생성자가 1개도 안나오면 그 수는 셀프넘버일것
    for i in range(1, a+1):
        s = i
        while True:
            # 각 자릿수 더해주기
            s += i % 10
            i = i // 10
            if i // 10 == 0:
                # 첫번째 자릿수에 도착했으면 그거까지 더해주고 멈춘다
                s += i % 10
                break
        # i + i의 각자릿수 합이 a와 같다면 i는 a의 생성자
        if s == a:
            # 생성자가 1개라도 있으면 바로 함수 멈춰준다.
            return
    # a 아래 모든 수 다확인해도 없으면 셀프넘버
    return a


for i in range(1, 10001):
    if self_number(i):      # 리턴값이 있으면 출력
        print(i)


# 방법 2

def self_number(a):
    # a보다 작은 모든수로 생성자 함수를 넣었는데
    # 생성자가 1개도 안나오면 그 수는 셀프넘버일것
    for i in range(1, a+1):
        s = i
        for j in str(i):
            s += int(j)
        # i + i의 각자릿수 합이 a와 같다면 i는 a의 생성자
        if s == a:
            # 생성자가 1개라도 있으면 바로 함수 멈춰준다.
            return
    # a 아래 모든 수 다확인해도 없으면 셀프넘버
    return a

for i in range(1, 10000):
    if self_number(i):      # 리턴값이 있으면 출력
        print(i)