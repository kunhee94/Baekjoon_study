# 첫번째 풀이 시간초과 남
n1 = int(input())
n2 = int(input())
sosu_li = []
for i in range(n1, n2 + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        sosu_li.append(i)

if len(sosu_li) > 0:
    print(sum(sosu_li))
    print(min(sosu_li))
else:
    print(-1)

# 두번째 풀이
# 원래는 항상 n1,n2의 모든 수를 확인했었지만
# 이방법이면 1과 자기자신사이에 약수가 1개라도 발견되는 즉시 소수로 판단 for문을 탈출하기 때문에
# 훨씬 빨리 풀수있음
n1 = int(input())
n2 = int(input())

sosu_list = []
for i in range(n1, n2 + 1):
    cnt = 0
    if i > 1:  # 1,1이 입력되었을땐 -1을 출력해야됨
        for j in range(2, i):  # 2부터 i-1까지
            if i % j == 0:
                cnt += 1
                break  # 2부터 i-1까지 나눈 몫이 0이면 cnt 증가하고 for문을 끝냄
        if cnt == 0:
            sosu_list.append(i)  # cnt ==0이면 소수리스트에 추가

if len(sosu_list) > 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)  # 소수 없으면 -1 출력해야됨