import sys
sys.stdin = open('../p3.txt')
def cond(x,n,k,i,hap):
    global L,F
    if hap > L: return
    if hap ==L:
        F = 1
        return F
    if k==i:
        return
    if x>=n: return
    else:
        chk[x]=1
        cond(x+1,n,k+1,i,hap+stick[x])
        chk[x]=0
        cond(x+1,n,k,i,hap)
T = int(input())
for tc in range(1,T+1):
    N,L = map(int, input().split())
    stick = list(map(int, input().split()))
    chk = [0]*N
    stick.sort()
    F = 0
    for i in range(1,N):
        cond(0,N,0,i,0) # 시작인덱스, 끝인덱스, 카운트, 카운트비교,합
    print('#%d %d' %(tc,F))


