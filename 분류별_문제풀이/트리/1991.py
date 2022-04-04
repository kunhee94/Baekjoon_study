import sys
sys.stdin = open("input.txt", "r")


def pre_order(k):
    global res
    res += k
    # 왼쪽 자식있으면
    if tree[k][0] != '.':
        pre_order(tree[k][0])
    # 오른자식도 있으면
    if tree[k][1] != '.':
        pre_order(tree[k][1])

def center_order(k):
    global res
    # 왼쪽 자식있으면
    if tree[k][0] != '.':
        center_order(tree[k][0])
    res += k
    # 오른자식도 있으면
    if tree[k][1] != '.':
        center_order(tree[k][1])

def back_order(k):
    global res
    # 왼쪽 자식있으면
    if tree[k][0] != '.':
        back_order(tree[k][0])
    # 오른자식도 있으면
    if tree[k][1] != '.':
        back_order(tree[k][1])
    res += k


V = int(sys.stdin.readline().rstrip())
tree = dict()
for i in range(V):
    p, c1, c2 = sys.stdin.readline().rstrip().split()
    tree[p] = [c1, c2]
res = ''
pre_order('A')
print(res)
res = ''
center_order('A')
print(res)
res = ''
back_order('A')
print(res)
