import sys
sys.stdin = open('../p3.txt')
# def cond(x,n,k):
#     if k==n:
#         print(chk)
#         return
#     if x>=n: return
#     else:
#         chk[x]=1
#         cond(x+1,n,k+1)
#         chk[x]=0
#         cond(x+1,n,k)
T = int(input())
for tc in range(1,T+1):
    N,L = map(int, input().split())
    stick = list(map(int, input().split()))
    stick.sort()
    # print(stick)
    i = N
    F = 0
    while True:
        i -=1
        minus = stick[i]
        if minus <= L:
            L -= minus
        if L in stick:
            F = 1
            break
        if L < stick[0]:
            break
    print('#%d %d' %(tc, F))



