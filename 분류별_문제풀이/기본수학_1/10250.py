t=int(input())
for i in range(t):
    h,w,n=map(int,input().split())
    f=n%h				# n을h로 나눈 나머지가 층수
    r=n//h+1			# 몫+1이 방번호
    if f==0:			# 대신 나머지가 0일 경우는 꼭대기 층이의 몫번호 방임
        print(h*100+(n//h))
    else:
        print(f*100+r)