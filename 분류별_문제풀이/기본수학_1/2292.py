# 6,12,18,24이렇게 증가함
#1 7 19 37 61...
a = int(input())
cnt=1
number=1
while a>number:
    number+=6*cnt
    cnt+=1

print(cnt)