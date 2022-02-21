# N개의 카드중 3개를 합쳐서 최댜한 M을 넘지않고 가까운 수
N,M=map(int,input().split())
card_num=list(map(int,input().split()))
l=len(card_num)
total=0
# 그냥 모든 경우의수 전부 다 해본다
for i in range(l-2):
    # 3중 for문을 이용하여 3개를 더하는 모든 경우의 수를 돈다
    for j in range(i+1,l-1):
        for k in range(j+1,l):
            # 만약 M보다 크다면 그냥 넘겨버림
            if card_num[i] + card_num[j] + card_num[k] > M:
                continue
            else:
                # M 보다 작으면 그전의 경우보다 큰지 비교하고 큰거 저장
                total=max(total,card_num[i] + card_num[j] + card_num[k])
