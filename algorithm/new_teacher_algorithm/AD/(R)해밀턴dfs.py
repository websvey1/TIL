import sys
sys.stdin = open('해밀턴.txt')

def dfs(x, cnt, hap):
    global result
    if hap>result:return
    if cnt==N:
        if data[x][0]:
            hap += data[x][0]
            if hap<result: result = hap
        return
    for i in range(1,N): # 앞을 내가 가볼 곳.
        if visit[i] : continue
        if data[x][i] ==0: continue   ####
        visit[i] = 1
        dfs(i, cnt+1, hap+data[x][i])
        visit[i] = 0
N = int(input())

data = [list(map(int, input().split()))for _ in range(N)]
visit = [0]*(N+1)
result = float('inf')
dfs(0,1,0) # 첫번째 도시, 시행횟수1, 합0
print(result)


#################################################
