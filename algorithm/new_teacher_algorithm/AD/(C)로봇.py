import sys
sys.stdin = open("로봇.txt")
def perm(x,n,hap):
    global result
    if hap>result:return
    if x==n:
        if result >hap:
            result = hap
    else:
        for i in range(n):
            if a[i] == 0:
                a[i] = 1
                perm(x+1, n, hap+data[x][i])
                a[i] = 0
#
#
# def perm(x,y,hap):
#     global result
#     if x == y:
#         if hap<result:
#             result = hap
#         return
#     else:
#         for i in range(y):
#             if a[i]:continue
#             if hap+data[x][i] >result:continue # 이거랑 아래꺼랑 바꾸면 왜 안돼지??..
#             a[i] = 1
#             perm(x+1,y,hap+data[x][i])
#             a[i]=0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    snack = list(map(int, input().split()))
    robot = list(map(int, input().split()))
    data = [[0 for _ in range(N)]for _ in range(N)]
    a = [0]*N
    rec = [0]*N
    result = float('inf')
    for i in range(N):
        for j in range(N):
            data[i][j] = abs(snack[i*2]-robot[j*2])+abs(snack[i*2+1]-robot[j*2+1])

    # print(data)
    perm(0,N,0)
    print(result)



