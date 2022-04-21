import sys
from collections import deque
sys.stdin = open("input.txt", "r")


S = int(input())

Q = deque()
visited = [0]*1000
# visited[1] = 1
# 현 화면
res = 'e'
# 클립보드
Q.append((res,0))
# 시간
final_time = 0
while Q:
    clib, time = Q.popleft()
    if len(clib) == S:
        final_time = time
        break
    if visited[len(clib)] == 0:
        # 복사해서 클립보드에 넣기
        Q.append((res+clib, time+1))
        # 클립보드에 있는 모든 이모티콘 화면에 붙여넣기
        copy = res+clib
        Q.append((copy, time+1))
        # 화면에 있는 이모티콘하나 삭제
        res = res[:-1]
        Q.append((res, time+1))
    visited[len(clib)] = 1

print(final_time)





