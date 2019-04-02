import sys
sys.stdin = open("로봇.txt")

def perm(x,n,hap):
    global result
    if x==n:
        if hap<result:
            print(a)
            result = hap
        return
    else:
        for i in range(x,n):
            a[i],a[x] = a[x],a[i]
            perm(x+1,n,hap+1)
            a[i], a[x] = a[x], a[i]
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    snack = list(map(int, input().split()))
    robot = list(map(int, input().split()))
    S = []
    R = []
    a = list(range(N))
    result = 0
    for i in range(0,N*2,2):
        S.append([snack[i],snack[i+1]])
        R.append([robot[i],robot[i+1]])
    # print(S,R)
    perm(0,N,0)