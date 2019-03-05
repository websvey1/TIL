import sys
sys.stdin = open("소수.txt")

a,b = list(map(int, input().split()))
data = [i for i in range(a,b+1)]

# 상근이형 소수
def sosu(a,b):
    sosu = list(range(b+1))
    root = int(b**0.5)
    sosu[1] = 0
    # print(sosu)
    for i in range(2, root+1):
        # if i in sosu:
        if sosu[i]:
            m = i+i
            while m < b+1:
                sosu[m] = 0
                m += i
    sosu = sosu[a::]
    sosu = [i for i in sosu if i]
    return sosu
result = sosu(a,b)

A = result
print(len(A))
print(A[0]+A[-1])







#인터넷 코드

# import sys
# sys.stdin = open("소수.txt")
# 
# L,M = list(map(int, input().split()))
# data = [i for i in range(L,M+1)]
# 
# a = [False,False] + [True]*(M-1)
# primes=[]
# 
# for i in range(L,M+1):
#   if a[i]:
#     primes.append(i)
#     for j in range(L*i, M+1, i):
#         a[j] = False
# print(primes)
# print(len(set(primes)))
# print(min(primes)+max(primes))