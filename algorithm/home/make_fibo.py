# # 일반적인 피보나치
# def fibo(n):
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
#
# print(fibo(35))

# 시행속도 102회


# # 메모이즘
# def fibo_1(n):
#     if n >=2 and len(memo) <=n:
#         memo.append(fibo_1(n-1)+fibo_1(n-2))
#     return memo[n]
#
# memo = [0, 1]
# print(fibo_1(35))
# 시행속도 52회
#
# #DP
# def fibo_2(n):
#     f=[0,1]
#     for i in range(2, n+1):
#         f.append(f[i-1]+f[i-2])
#     return f[n]
# print(fibo_2(35))
# # # 시행속도 17회