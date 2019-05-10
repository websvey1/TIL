def dfs(n,cnt):
    global F
    if F: return
    if n == N:
        # print(sum(box))
        if sum(box) == K:
            F = 1
            return
        return
    else:
        box[cnt] = data[n]
        dfs(n+1, cnt+1)
        if F: return
        box[cnt] = 0
        dfs(n+1, cnt)

T = int(input())
for tc in range(1,T+1):
    N,K = map(int, input().split())
    data = list(map(int, input().split()))
    box = [0]*N
    cnt = 0
    F = 0
    dfs(0,cnt)
    if F:
        print('YES')
    else:
        print('NO')


