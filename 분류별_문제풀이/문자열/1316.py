t = int(input())         # 첫줄에 단어갯수 들어옴
total = 0                # 그룹단어 갯수
for _ in range(t):     # 단어갯수만큼 단어 받아야함
    word = input()
    re_word = ''				# 비교할 문자열
    for i in range(len(word)):      # 단어를 인덱스로 돌자
        if i == 0:
            # 첫번째 알파벳은 비교대상없으니까 더해줌
            re_word += word[i]
        elif word[i] in re_word and word[i] == word[i-1]:
            # 이미 문자열에 있지만 연속일경우는 더해줘야됨
            re_word += word[i]
        elif word[i] in re_word and word[i] != word[i-1]:
            # 이미 문자열에 있고 연속이 아니면 더하면 안됨
            continue
        else:
            re_word += word[i]	# 위경우가 아닌경우 걍 더해주면됨
    if re_word == word:			# 이렇게해서 만든 문자열이 기존과 같으면 그룹단어임
        total += 1
    re_word = ''	            	# 비교할 문자열 초기화 시켜주고 다시 돌림
print(total)