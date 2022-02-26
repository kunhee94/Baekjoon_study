x_y = [[0 for i in range(101)] for j in range(101)]
# 100x100좌표평면 만든다
for i in range(4):
    x1,y1,x2,y2 = map(int, input().split())
    for x in range(x1,x2):		# 사각형이면 1을 더해야 되는데 주어진 꼭짓점 갯수만큼 더하면
        for y in range(y1,y2):	# 1개씩 더많이 계산되니까 range 범위를 이렇게 잡아줌
            x_y[x][y] = 1		#이렇게 x,y위치를 1로 변환시켜주면 겹쳐도 영향 안받음

result =0
for i in range(101):
    for j in range(101):
        if x_y[i][j] == 1: # 이제 좌표평면 리스트를 돌면서 색칠해둔 부분들 세면 됨
            result += 1
print(result)