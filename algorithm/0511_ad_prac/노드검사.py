import sys
sys.stdin = open('노드검사.txt')
def dfs(n):
    global flag
    if n==G:
        flag = 1
        return
    for i in range(1,len(data)):
        if data[n][i] == 1 and visit[i] ==0:
            visit[n] = 1
            dfs(i)
T = int(input())
for tc in range(1,T+1):
    V,E = map(int, input().split())
    data =[[0 for _ in range(V+1)] for _ in range(V+1)]
    visit = [0] * (V+1)
    flag = 0
    # print(data)
    for e in range(E):
        a,b = map(int, input().split())
        # print(a,b)
        data[a][b] = 1
    # for i in range(V+1):
    #     print(*data[i])
    S,G = map(int, input().split())
    a = dfs(S)
    print('#%d %d' %(tc, flag))
