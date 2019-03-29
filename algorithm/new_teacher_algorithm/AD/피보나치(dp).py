def fib(n):
    f = [1,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

# def fibo(n):
#     if n <2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
N = int(input()) -1
f = [1,1]
# print(fibo(N))
print(fib(N))

