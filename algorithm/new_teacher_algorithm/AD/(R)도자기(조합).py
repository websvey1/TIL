import sys
sys.stdin = open('도자기(조합).txt')
def dfs(x,n,cnt):
    global result
    if cnt ==M:
        for i in range(cnt):
            print(rec[i], end=" ")
        print()
        result +=1
    # if x==n:
    #     return #N개가아니라 M개를 고르는거다.!


    else:
        백업변수 = 0
        for i in range(x,N): # 조합이므로,  x부터,....
            if 백업변수 ==data[i]:continue
            # if rec[cnt] == data[i]:continue # 같은재료이면 스킵
            rec[cnt] = data[i]
            백업변수 = data[i]
            dfs(i+1, n, cnt+1)
        # rec[cnt] = 0 # 지우는 시점이 중요하다. for문을 돌면서

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    data = sorted(list(map(int, input().split())))
    rec = [0] * N
    result = 0
    dfs(0,N,0)
    print(data)