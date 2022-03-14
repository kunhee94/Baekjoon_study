import sys
sys.stdin =open("input.txt", "r")
sys.setrecursionlimit(2000)

# 내가짠거
def DFS(gr,start):
    # 방문한적 없다면 방문체크
    if start not in visited:
        visited.append(start)
    # 여기서 백트래킹 조건을 안달아서 런타임 에러가 발생
    else:
        return
    # 연결된 노드 없으면 종료
    if gr[start] == []:
        return
    else:
    # 각 노드에 연결된거 하나씩 돈다
        for i in range(len(gr[start])):
            DFS(gr, gr[start][i])
# 구글링버전
def DFS(gr, start):
    for i in gr[start]:
        if i not in visited:
            visited.append(i)
            DFS(gr, i)

T = int(input())
node = int(input())
graph = dict()
for i in range(1, T+1):
    graph[i] = []

for tc in range(node):
    k, v = map(int, (input().split()))
    graph[k].append(v)

visited = []
DFS(graph, 1)

print(len(visited)-1)

