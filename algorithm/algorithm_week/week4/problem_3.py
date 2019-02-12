import sys
sys.stdin = open('problem_3.txt', "r")

def DFS(start):
    visit[start] = 1

    if start in data:
        for i in data[start]:
            if visit[i] == 0:
                DFS(i)

T = int(input())
for tc in range(1, 1+T):
    V,E = map(int, input().split())
    data = {}
    visit = [0 for _ in range(V+1)]
    for e in range(E):
        a,b = map(int, input().split())
        if a not in data.keys():
            data[a] = [b]
        else:
            data[a] += [b]
    S, G = map(int, input().split())
    # if G ==data.pop(data.pop(S)):
    #     print("성공")
    # print(data.pop(S))
    # print(data)
    # print(f'{tc} {data} {S,G}')
    DFS(S)
    print(f'#{tc} {visit[G]}')

#
#
# for tc in range(T):
#     V, E = map(int, input().split())
#     node_dict = {}
#     visit = [0 for _ in range(V+1)]
#
#     for _ in range(E):
#         k,v = map(int, input().split())
#         if not k in node_dict:
#             node_dict[k] = []
#         node_dict[k] += [v]
#     S, G = map(int, input().split())
#     print(node_dict)
#     DFS(S)
#
#
#     print(f'#{tc+1} {visit[G]}')
