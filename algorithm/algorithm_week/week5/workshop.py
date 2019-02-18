import sys
from pprint import pprint

sys.stdin = open("workshop.txt")
for tc in range(1, 11):
    N = int(input())
    cnt = 0
    data = []
    re_data = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(N):
        data.append(list(map(int, input().split())))
        # while cnt <len(data):
        # result = []
        # for j in range(len(data)):
        #     for k in range(len(data)):
        #         re_data[k][j] = data[j][k]
        #
        # for l in range(len(re_data)):
        #     if re_data[l] == 1:
        #         result.append(re_data[l])
    for j in range(len(data)):
        for k in range(len(data)):
            if data[k][j] == 2:
                data[k][j] == 0