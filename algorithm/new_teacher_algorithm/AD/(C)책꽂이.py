import sys
sys.stdin = open('책꽂이.txt')
def perm(x,n,hap):
    global MMAAXX
    if x==n:
        if MMAAXX > hap and hap >=B:
            MMAAXX = hap
    else:
        perm(x+1,n,hap)
        if hap + data[x] > MMAAXX:
            return
        arr[x] = 1
        perm(x+1,n, hap+data[x])
        arr[x] = 0
T = int(input())
for tc in range(1,T+1):
    N,B = map(int, input().split())
    data = sorted([int(input())for _ in range(N)])
    # print(data)
    arr = [0] * N
    MMAAXX = float('inf')
    perm(0,N,0)
    print(MMAAXX-B)