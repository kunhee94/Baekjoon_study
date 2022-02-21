a, b, v=map(int,input().split()) 		# 공식자체는 맞는데 시간초과가 남
result = 0							# 어덯게 해결하지?
day = 0
while True:
    result += a
    day += 1
    if result >= v:
        print(day)
        break
    result -= b

# 새로만든 답안
a, b, v = map(int,input().split())
high = (v-b)/(a-b)      # 이랬을때 high가 정수면 그냥 몫을 구하면되고 분수면 +1해서
if high % 1 == 0:	    # 구하면됨
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)