def dfs(N,k):
    if k==0:
        print(visit)
    elif N < k:
        # print(visit)
        return
    else:
        visit[k-1] = a[N-1]
        dfs(N-1, k-1)
        dfs(N-1, k)
        # for i in range(k,N):
        #     visit[i] = a[i]
        #     dfs(N,k+1)
#             visit[i] = 0

a = [1,2,3,4,5]
N = len(a)
visit = [0]*3
flag = 0
dfs(N,3)