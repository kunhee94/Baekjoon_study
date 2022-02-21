t = int(input())
fin_score = 0
cnt = 0
for i in range(t):  # 일단 t만큼 실행해야함
    scores = list(map(int, input().split()))  # 그다음 입력값을 리스트로 만들어서 받아줌
    score_cnt = scores[0]  # 리스트[0]만큼 실행해야 하니까 따로 빼줌
    for j in range(1, score_cnt + 1):
        fin_score += scores[j]  # 리스트[1]부터 끝까지 더해야함
    st_avg = fin_score / score_cnt  # 전부 더한 값을 리스트[0]으로 나눠서 그 리스트의
                                    # 평균 반환
    for l in scores:  # 평균 이상 값 찾아야 됨
        if l == score_cnt:  # 리스트[0]은 갯수세는 대상에서 제외임
            continue
        elif l > st_avg:  # 평균 값이상일때 갯수를 세준다
            cnt += 1
    result = cnt / score_cnt * 100  # 이제 갯수 센거를 리스트[0]으로 나눈 후 *100을 해서
                                    # 평균이상의 비율을 구한다.
    print(f'{result:0.3f}' + '%')  # f스트링으로 소숫점 3자리까지만 나오게 설정
    cnt = 0
    fin_score = 0  # 한바퀴 돌았으니 누적을 막기위해 초기화

# 아래 방식으로 하면 코드길이를 굉장히 줄일 수 있음
t = int(input())
for _ in range(t):
    result = list(map(int, input().split()))
    avg = sum(result[1:]) / result[0]  # 슬라이싱과 sum함수로 길이 단축
    count = 0
    for i in result[1:]:  # 마찬가지로 슬라이싱 활용
        if i > avg:
            count += 1

    result2 = count / result[0] * 100
    print('%.3f%%' % result2)