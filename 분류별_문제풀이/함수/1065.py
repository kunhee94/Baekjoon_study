

X = input()

def hansu(N):
    # 한자릿수는 비교할 뒷자리도 없고 어차피 한수임
    if len(N) == 1:
        return True
    # 두자릿수 부터는 각 자릿수의 차를 set에 저장해서
    else:
        result = set()
        for i in range(1, len(N)):
            result.add(int(N[i-1]) - int(N[i]))
            # 만약 set길이가 1보다 커지면 한수가아님
            if len(result) > 1:
                return False
        # 다확인했는데 set길이가 1이면 한수임
        if len(result) == 1:
            return True

cnt = 0

for i in range(1, int(X)+1):
    if hansu(str(i)):
        cnt += 1

print(cnt)
