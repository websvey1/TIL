# def f(n):
#     if n <2:
#         return 1
#     else:
#         return f(n-1) + f(n-2)
# print(f(7))

# f = lambda n : f(n-1)+f(n-2)
# f(4)



# 피보나치 람다
# fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
# print(fib(8))


#   동적할당 !
# def fibo(n):
#     # global memo
#     if n>=2 and len(memo) <=n:
#         memo.append(fibo(n-1) + fibo(n-2))
#     return memo[n]
# memo = [0,1]
# print(fibo(8))

# 피보나치 DP 적용 알고리즘
def fibo2(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(fibo2(100000))