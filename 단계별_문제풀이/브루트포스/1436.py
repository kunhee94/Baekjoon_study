import sys
sys.stdin =open("input.txt", "r")

N = int(input())

# 겹치는거 제거하기 위해 셋 사용
result = set()
i = 666
while len(result) <= N:
    for j in range(1, len(str(i)) - 1):
        if str(i)[j - 1] == str(i)[j] == str(i)[j + 1] == '6':
            result.add(i)
    i += 1
# 다시 정렬해서 순서대로 뽑아야하니까 리스트로 형변환
a = list(result)
# 리스트 인덱스 활용해서 답출력
print(sorted(a)[N-1])
