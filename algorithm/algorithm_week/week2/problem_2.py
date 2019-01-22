import sys
sys.stdin = open("problem_2.txt", "r")


arr = list(range(1, 13))
n = len(arr)
T = int(input())
for test_case in range(1, (T + 1)):
    N, K = map(int, input().split())
    # print(N, K)
    cnt = 0
    for i in range(1<<n):
        PEP = []
        for j in range(n+1):
            if i & (1<<j):
                PEP.append(arr[j])
        if len(PEP) == N and sum(PEP) ==K:
            cnt += 1
    print(f'#{test_case} {cnt}')
############################ 준석이코드 #######
# A = list(range(1, 13))
# n = len(A)
# T = int(input())
# for i in range(1, T+1):
#     N, K = map(int, input().split())
#     result = 0
#     for j in range(1<<n):
#         L = []
#         for k in range(n):
#             if j & (1<<k):
#                 L.append(A[k])
#
#         if len(L) == N:
#             L_sum = 0
#             for k in L:
#                 L_sum += k
#             if L_sum == K:
#                 result += 1
#
#     print(f"#{i} {result}")