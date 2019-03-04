import sys
sys.stdin = open("연속부분최대곱.txt")
# T = int(input())
# gop = 1
# # for tc in range(1, T+1):
# #     data.append(float(input()))
# data = [float(input()) for i in range(T)]
# for i in range(T):
#     for j in range(T-i):
#         if gop < gop*data[j]:
#             gop *= data[j]
#         else:
#             gop = 1
#     print(gop)


# print(format(gop, '.3f'))
########## 세민이형
n = int(input())
data = [float(input()) for i in range(n)]

print(data)

max_product = 1
now = 1
count = 0
for i in range(n):

    if now*data[i] < 1:
        now = 1
    else:
        if now*data[i] > max_product:
            max_product = now*data[i]
        now = now*data[i]

if max_product > 1:
    print('%.3f' % max_product)
else:
    print('%.3f' % max(data))

