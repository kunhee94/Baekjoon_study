def same_left_right(M):
    global switch
    # switch[M-1]을 중심으로 좌우 대칭을 확인해서 제일 긴것을 찾아야한다.
    result = 0
    for j in range(len(switch)):
        # 인덱스 범위 내에서 j를 늘려가며 확인
        if 0 <= M - 1 - j and M - 1 + j < len(switch):
            if switch[M - 1 - j] == switch[M - 1 + j]:
                result = j
            # 대칭이 아니면 바로 for문 종료해야한다!!!!!
            else:
                break
    # 제일 긴거 찾았으면 리턴
    return result

N = int(input())  # 스위치 갯수
switch = list(map(int, input().split()))    # 스위치 현상태
student_N = int(input())      # 학생 수
for _ in range(student_N):
    sex, card_number = map(int, input().split())
    # 남자면
    if sex == 1:
        for j in range(N):
            # (j+1)이 card_number의 배수고 switch[j]가 1이면 0으로 바꾼다
            if (j + 1) % card_number == 0:
                if switch[j]:
                    switch[j] = 0
                    # (j+1)이 card_number의 배수고 switch[j]가 0이면 1로 바꾼다
                else:
                    switch[j] = 1
    # 여자면
    elif sex == 2:
        # 받은 카드 좌우대칭 제일 긴것 찾기
        long = same_left_right(card_number)
        # long만큼 돌면서 스위치 바꾸기
        for j in range(long+1):
            # 1이면 0으로 바꿔주기
            if switch[card_number - 1 + j] == 1:
                switch[card_number - 1 - j], switch[card_number - 1 + j] = 0, 0
            # 0이면 1로 바꿔주기
            elif switch[card_number - 1 + j] == 0:
                switch[card_number - 1 - j], switch[card_number - 1 + j] = 1, 1

# 한줄에 20개씩만 출력해야함
count = 0  # 20개 출력을 위한 변수 선언
while count < len(switch):
    print(switch[count], end=" ")
    if count % 20 == 19: # 0~19까지만 한줄에 출력되게 하기 위해
        print()
    count += 1