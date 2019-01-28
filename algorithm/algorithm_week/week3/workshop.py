import sys
sys.stdin = open("workshop.txt", "r")
# T = int(input())
# # ZRO, ONE, TWO, THR, FOR, FIV, SIX, SVN, EGT, NIN = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# for tc in range(1, T+1):
#     temp = input() # dummy
#     data = list(map(str, input().split()))
#     sort_data_0 = ''
#     sort_data_1 = ''
#     sort_data_2 = ''
#     sort_data_3 = ''
#     sort_data_4 = ''
#     sort_data_5 = ''
#     sort_data_6 = ''
#     sort_data_7 = ''
#     sort_data_8 = ''
#     sort_data_9 = ''
#     sort_total = ''
#     # print(temp)
#     for i in data:
#         # ZRO, ONE, TWO, THR, FOR, FIV, SIX, SVN, EGT, NIN = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#         if i == 'ZRO':
#             sort_data_0 += 'ZRO '
#         if i == 'ONE':
#             sort_data_1 += 'ONE '
#         if i == 'TWO':
#             sort_data_2 += 'TWO '
#         if i == 'THR':
#             sort_data_3 += 'THR '
#         if i == 'FOR':
#             sort_data_4 += 'FOR '
#         if i == 'FIV':
#             sort_data_5 += 'FIV '
#         if i == 'SIX':
#             sort_data_6 += 'SIX '
#         if i == 'SVN':
#             sort_data_7 += 'SVN '
#         if i == 'EGT':
#             sort_data_8 += 'EGT '
#         if i == 'NIN':
#             sort_data_9 += 'NIN '
#     sort_total = sort_data_0 + sort_data_1+sort_data_2 + sort_data_3 + sort_data_4 + sort_data_5 + sort_data_6 + sort_data_7 + sort_data_8 + sort_data_9
#     print(f'#{tc}\n{sort_total}')


    # #성원이형
    # test = int(input())
    # num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # for tc in range(test):
    #     input_number = input().split()
    #     input_list = input().split()
    #     num_count_list = [0] * 10
    #     for i in range(10):
    #         num_count_list[i] = input_list.count(num_list[i])
    #
    #     print(input_number[0])
    #     for i in range(len(num_count_list)):
    #         print(f"{num_list[i]} " * num_count_list[i], end="")
    #     print()

    # 상근이형
T = int(input())
for p in range(T):
    input()
    b = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    for c in input().split(): b[c] += 1
    print(f"#{p + 1}\n", *[(k + " ") * v for k, v in b.items()], sep="")
    # liszt = []
    # for key, value in b.items():
    #     liszt.append((key+ " ")*value, sep="")