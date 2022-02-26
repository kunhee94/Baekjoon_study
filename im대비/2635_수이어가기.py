n = int(input())

nums = []

for i in range(n+1): # n이하의 모든 양수를 돌아야하니까
    nums2 = []
    first = n
    second = i
    third = n-i
    nums2 = [first,second, third] # 기본세팅
    k = 2			# 인덱스 2부터 nums2[k-1]-nums2[k]를 계속적으로 실행해줘야함
    while True:
        new_num = nums2[k-1]-nums2[k]
        if new_num < 0:		# new_num이 음수면 더하지 않고 반복문종료
            break
        nums2.append(new_num) # 양수면 계속 while돌면서 num2에 추가
        k += 1				# 인덱스 오른쪽으로 한칸씩 이동하면서 반복문 돌려야됨
    nums.append(nums2)		# 음수 떠서 반복문 나왔으면 빈리스트에 넣고 다음 양수 다시 돈다
cnts = []
for i in nums:
    cnts.append(len(i))		# nums의 각 리스트의 길이 비교해야됨

result_cnt = max(cnts)		# 젤 긴거 길이 출력
print(result_cnt)
for i in nums:				# 젤 긴거 리스트 출력해야됨
    if len(i) == result_cnt:
        print(*i, end=" ")	# 리스트 그대로 출력했다가 틀림 언패킹하자