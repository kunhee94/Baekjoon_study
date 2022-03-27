# 60-(45-M) M<45일때 45분당기면 몇분인지 구하는거 생각해내느라 오래걸림
# +백준테스트할 때 예시 출력만 확인하고 넣지말고 남는 케이스 다생각해내자
# 괜히 예시만 입력했다가 다른 코드 빼먹음

a = list(map(int, input().split()))
H = a[0]
M = a[1]
h = 0
m = 0
if M - 45 < 0 and H > 0:
    h = H - 1
    m = 60 - (45 - M)
elif M - 45 >= 0 and H > 0:
    h = H
    m = M - 45
elif M - 45 < 0 and H == 0:
    h = 23
    m = 60 - (45 - M)
elif M - 45 >= 0 and H == 0:
    h = 0
    m = M - 45

print(h, m)