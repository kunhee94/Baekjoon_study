alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'   # 출력을 대문자로 해야하니 대문자 알파벳 문자열 하나 만든다
a=input()
word=a.upper()					    # 비교를 위해선 입력값을 전부 대문자로 바꿔준다
result=[]
for i in alph:
    result.append(word.count(i))    # 알파벳 돌면서 문자열에 각 알파벳이 몇번씩 나왔는지 세주고 빈리스트에 순서대로 저장
mt=max(result)					    # 채운 리스트에 가장 많이 등장한 알파벳의 등장횟수 찾아줌
many=result.count(mt)			    # max값이 여러개인지 확인
k=result.index(mt)				    # 리스트의 인덱스==알파벳의 위치
if many==1:							# max값이 1개면 그 인덱스위치의 알파벳을 프린트하면 됨
    print(alph[k])
else:
    print('?')   				    # max값이 여러개면 '?'출력해야함