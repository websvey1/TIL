# T = 5
# data = ['213', '61', '153', '95', '753']
# num = []
# # for tc in range(T):
# #     data.append(input())
# #
# # for i in range(len(data)):
# #     hap = 0
# #     for j in range(len(data[i])):
# #         hap += int(data[i][j])
# #     # print(hap)
# #     if hap.index(max(hap))
# # print(data, num)
#
#
# def root_calc(n):
#     while True:
#         a = 0
#         while n:
#             a += n % 10
#             n = n // 10
#         if a < 10:
#             return a
#         n = a
# # print(root_calc(2913))
# root_max = 0
# sol = 0
# for i in range(5):
#     root = root_calc(data[i])
#     if root_max < root :
#         root_max = root
#         sol = data[i]
#     if root_max == root:
#         if sol > data[i]:
#             sol = data[i]
# print(sol)