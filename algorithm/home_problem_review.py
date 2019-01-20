# import sys
# sys.stdin = open("input_1.txt")
#
# T = int(input())
# for test_case in range(1, T +1):
#     N = int(input())
#     data = list(map(int, input().split()))
#     # print(data)
#     max_num = data[0]
#     min_num = data[0]
#     for i in range(0, len(data)):
#         if data[i] > max_num:
#             max_num = data[i]
#         if data[i] < min_num:
#             min_num = data[i]
#         dif = max_num - min_num
#     print(f'#{T}', dif)
############################################################## 위 1번

import sys
sys.stdin = open("input_2.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    K, N, M= list(map(int, input().split()))
    M_num =  list(map(int, input().split()))
    for i in range(1, len(M_num)):
        M_num_difference = 0
        if M_num[i] - M_num[i-1] > M_num_difference:
            M_num_difference = M_num[i] - M_num[i-1]
    if M_num_difference > K-1:
         
        # M_num_difference.append(M_num[i+1]-M_num[i])
        print(M_num_difference)
    # print(M_num)
    # c = [0]*N
    # for i in range(len(M_num)):
    #     c[M_num[i]] += 1
    # print(c)

# T = int(inp