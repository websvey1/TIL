# import sys
# sys.stdin = open("problem_input.txt")
# T = 10
# for i in range(T):
#     ans = 0
#     N = int(input())
#     data = list(map(int, input().split()))
#     # print(data)
#     for j in range(2, len(data)-2):
#         if data[j] > max(data[j-2], data[j-1], data[j+1], data[j+2]):
#             ans += data[j] - max(data[j-2], data[j-1], data[j+1], data[j+2])


# import sys
# sys.stdin = open("problem_input.txt")
# T = 10
# for i in range(T):
#     ans = 0
#     N = int(input())
#     data = list(map(int, input().split()))
#     for j in range(2, len(data)-2):
#         if data[j-1] < data[j] and data[j-2] < data[j] and data[j+1] < data[j] and data[j+2] < data[j] :
#             ans += data[j] - max(data[j-2], data[j-1], data[j+1], data[j+2])
#     print("#{} {}".format(i+1, ans))

## 교수님 코드
import sys

sys.stdin = open("problem_input.txt")
T = 10
for i in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    print(data)
    # for j in range(2, N-2):
    #     min = 987654321
    #     for k in range(5):
    #         if k != 2:
    #             if data[j]-data[j-2+k] < min:
    #                 min = data[j] - data[j-2+k]
    #     if min >0:
    #         ans += min
    #
    # print("#{} {}".format(i+1, ans))