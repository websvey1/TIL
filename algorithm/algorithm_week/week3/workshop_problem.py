import sys
from pprint import pprint
# def hodol(data, 100, M):
#     M = 100
#     for i in range(100):
#         for j in range(M):
#             if data[i][j:M] == data[i][j:M][::-1]:
#                 return data[i][j:M]
#
sys.stdin = open("workshop_problem.txt", "r")
for T in range(10):
    tc = input()
    data = [input() for x in range(100)]
    for i in range(len(data)):
        start, end = 0, 100
        result = 0
        for j in range(len(data[i])):
            if data[i][start:end] != data[i][start:end][::-1]:
                start += 1
                for k in range(len(data)):
                    data[i][start:end] != data[i][start:end][::-1]:
                    start += 1
            elif:
            else:
                result = end - start
    print(result)

