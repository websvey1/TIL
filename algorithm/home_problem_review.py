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

# T = int(input())
# for test_case in range(1, T + 1):
#     K, N, M= list(map(int, input().split()))
#     M_num =  list(map(int, input().split()))
#     print(M_num)
#     c = [0]*N
#     for i in range(len(M_num)):
#         c[M_num[i]] += 1
#         for j in range(len(c)):
#             if c[j] == 0

T = int(input())
for tc in range(T):
    ans = 0
    k, n, m = map(int, input().split())
    data = list(map(int, input().split()))
    charge = [0] * (n + 1)
    charge[n] = 1

    # print(data)

    for i in range(len(data)):
        charge[(data[i])] = 1
    # print(charge)
    count = 0
    point = k

    while True:
        if charge[point] != 1:
            point += -1
        elif charge[point] == 1:
            count += 1
            charge = charge[point:]
        point = k
        if len(charge) == k:
            count += -1
            break
    if point == 0:
        count = 0
        break

    print(f"#{n}{count}")