#회문.
import sys
sys.stdin = open("problem_2.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input() for x in range(N)]
    data2 = [''.join([data[y][x] for y in range(N)]) for x in range(N)]
    result = ''
    for i in range(N):
        for j in range(N-M+1):
            if data[i][j:M+j] == data[i][j:M+j:][::-1]:
                result = data[i][j:j+M]
    # print(result)
    for i in range(N):
        for j in range(N-M+1):
            if data2[i][j:M+j] == data2[i][j:M+j:][::-1]:
                result = data2[i][j:j+M]
    # print(result)
    print(f'#{tc} {result}')

    ###
from pprint import pprint

# data = [str(_) * 10 for _ in range(10)]
# data2 = [''.join([data[x][y] for x in range(len(data[y]))]) for y in range(len(data))]
#
# # 여기부터 분석해봐
# data3_i = []
# data3 = []
# for y in range(len(data)):
#     for x in range(len(data[y])):
#         data3_i.append(data[x][y])
#     data3.append(''.join(data3_i))
#     data3_i = []
# # print(data3)
# # 끝
#
# print(data)
# print(data2)
# print(data3)