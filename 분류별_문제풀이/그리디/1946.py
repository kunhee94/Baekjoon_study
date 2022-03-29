import sys
sys.stdin = open("input.txt", "r")

# T = int(sys.stdin.readline().rstrip())
# for _ in range(T):
#     N = int(sys.stdin.readline())
#     score = [list(map(int, sys.stdin.readline().rstrip().split()))for _ in range(N)]
#     score.sort()
#     # print(score)
#     lis = score[:]
#     for i in range(len(score)):
#         for j in range(len(score)):
#             if i != j:
#                 # 면접이나 서류 둘다 높은 사람이 있으면 탈락
#                 if score[i][0] > score[j][0] and score[i][1] > score[j][1]:
#                     lis.remove(score[i])
#                     break
#     print(len(lis))

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline())
    score = [list(map(int, sys.stdin.readline().rstrip().split()))for _ in range(N)]
    score.sort()
    cnt = 1
    k = score[0]
    for i in range(1, len(score)):
        if score[i][1] < k[1]:
            cnt += 1
            k = score[i]
    print(cnt)

