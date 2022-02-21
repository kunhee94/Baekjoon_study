t = int(input())

result = 0							# 생성자가 없다면 0을 출력

for i in range(1,t+1):
    num = list(map(int, str(i)))	# i의 각 자릿수를 더하기 위해 스트링으로 형변환 후
    s_num = i + sum(num)			# map으로 각 자릿수를 다시 인트로 형변환해서 넣은 후
    if s_num == t:					# 다더해서 t랑 비교
        result = i					# 같다면 제일 작은 생성자
        break						# 젤 작은 생성자 뽑고 멈춰야됨
print(result)