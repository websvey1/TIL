import sys
sys.stdin = open("연속부분최대곱.txt")
T = int(input())
comp = 1
max_num = 0
data = [float(input()) for i in range(T)]
for i in range(T):
    if comp * data[i] < 1:
        comp = 1
    else:
        if comp*data[i] > max_num:
            max_num = comp*data[i]
        comp = comp*data[i]
if max_num > 1:
    print('%.3f' %max_num)
else:
    print('%.3f' %max(data))
# print(format(gop, '.3f'))
########## 세민이형
# n = int(input())
# data = [float(input()) for i in range(n)]
#
# print(data)
#
# max_product = 1
# now = 1
# for i in range(n):
#
#     if now*data[i] < 1:
#         now = 1
#     else:
#         if now*data[i] > max_product:
#             max_product = now*data[i]
#         now = now*data[i]
#     print(max_product, now)
# if max_product > 1:
#     print('%.3f' % max_product)
# else:
#     print('%.3f' % max(data))

