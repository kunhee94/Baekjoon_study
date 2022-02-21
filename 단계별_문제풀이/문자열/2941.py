c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
a=word
for i in c :
    a = a.replace(i, '*')  # 기존 문자열을 수정하는게 아니고
                            # 수정값을 반환하는 메소드니까 아예 수정값을 다시 기존 문자열에 할당해버리면
print(len(a))			   # 깔끔하게 문제해결