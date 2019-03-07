import sys
sys.stdin = open("../연속부분최대곱.txt")
N = int(input())
arr = []
for i in range(N):
    arr.append(float(input()))



# print(arr)
# mul = 1.0
# max = 0.0
# for i in range(N):
#     mul = 1.0
#     for j in range(i, N):
#         # if arr[i]*arr[j] >1:
#         #     sol = arr[i]*arr[j]
#         # else:
#         mul *=arr[j]
#         if mul>max:
#             max=mul
# print(max)



############## 1 for
mul = 1.0
max = 0.0
for i in range(N):
    mul *= arr[i]
    if mul <arr[i]:
        mul = arr[i]
    if mul>max:
        max=mul