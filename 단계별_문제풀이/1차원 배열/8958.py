t=int(input())
total=0     #O가 나올때마다 더해줄값
c=1			#O가 연속적으로 나올때 더해줄 값이 느니까
for i in range(t):		#일단 t만큼 실행해야 한다
    OX=input()			#그후 문자열을 받아준다.
    for j in OX:		#받은 각 문자열을 돈다.
        if j=='O':
            total+=c	#j=='O'이면 1을 더한다
            c+=1		#연속적으로 나타나면 나타난만큼 더해줘야됨
        else:
            c=1			#만약 X가 나오면 연속으로 누적된 점수 초기화 시켜줘야함
    print(total)		#각 문자열의 total값 출력
    total=0				#한 문자열 다돌았으니 total과 c를 초기화시켜줘야함