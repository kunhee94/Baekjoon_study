
arr = [list(map(int, input().split()))for _ in range(5)]

MC = [list(map(int, input().split()))for _ in range(5)]

call_mc = []
# mc가 부르는 수 1차원리스트로 만들기
for x in range(5):
    for y in range(5):
        call_mc.append(MC[x][y])

# 부른거 정리할 배열
called = [[0]*5 for _ in range(5)]

for i in range(len(call_mc)):
    cnt = 0
    for x in range(5):
        for y in range(5):
            # 사회자가 부른 숫자 위치에 체크
            if call_mc[i] == arr[x][y]:
                called[x][y] = 1
                break
    # 빙고체크 시작
    # 가로 체크
    for x in range(5):
        if sum(called[x]) == 5:
            cnt += 1
    # 대각선체크
    s1 = 0
    for x in range(5):
        s1 += called[x][x]
    if s1 == 5:
        cnt += 1
    # 반대 대각선 체크
    s2 = 0
    for x in range(5):
        s2 += called[x][4-x]
    if s2 == 5:
        cnt += 1
    # 세로 체크
    for y in range(5):
        s3 = 0
        for x in range(5):
            s3 += called[x][y]
        if s3 == 5:
            cnt += 1
    # cnt가 3이상이면 빙고임
    if cnt >= 3:
        # 부른 횟수는 i+1임
        print(i+1)
        break

