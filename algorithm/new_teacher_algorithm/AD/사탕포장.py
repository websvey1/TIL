import sys
sys.stdin = open("사탕포장.txt")

N = int(input())
data = list(map(int, input().split()))
result = 0

for i in range(N-1):
    for j in range(i,i+2):
        for k in range(j+1,N):
            if data[j] > data[k]:
                data[j], data[k] = data[k], data[j]
    data[i+1] += data[i]
    result += data[i+1]
print(result)

























#################################
############단순정렬###############
#################################
# for k in range(N-1): # k위치에서 2개씩만 정렬
#     for i in range(k, k+2):
#         for j in range(i+1, N):
#             if data[i] > data[j]:
#                 data[i], data[j] = data[j] , data[i]
#     data[k+1] += data[k] #K, K+1번째 포장
#     result += data[k+1] # 포장 누계
# print(result)
#################################
############삽입정렬###############
#################################
# data.sort()               # 정렬 후 적용
# for k in range(1,N):      #
#     data[k] += data[k-1]
#     result += data[k]
#     temp = data[k]
#     for i in range(k+1, N):
#         if data[i] < temp:  # 크거나 같은때까지 교환
#             data[i],data[i-1]= data[i-1],data[i]
#         else: break
# print(result)