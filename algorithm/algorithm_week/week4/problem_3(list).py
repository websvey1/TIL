import sys
sys.stdin = open('problem_3.txt', "r")
T = int(input())
for tc in range(1, 1+T):
    V,E = map(int, input().split())
    data = []
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
    print(data)
    # print(f'{tc} {data} {S,G}')
#


# def DFS(start):
#     visit[start] = 1
#
#     if start in node_dict:
#         for i in node_dict[start]:
#             if visit[i] == 0:
#                 DFS(i)
#