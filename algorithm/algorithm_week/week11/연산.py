import sys
sys.stdin = open('연산.txt')
def bfs(N,cnt):
    global M
    data = [1, -1, 2, -10]
    que = []
    que.append((N,cnt))
    visit[N] = 1
    f = -1
    while que:
        f +=1
        # x,cc = que.pop(0)
        x,cc = que[f]
        for i in range(len(data)):
            if i ==2:
                nx = x*data[i]
            else:
                nx = x+data[i]
            if nx <0 or nx>1000000: continue
            if visit[nx] == 1: continue
            if nx == M: return cc+1
            else:
                que.append((nx,cc+1))
                visit[nx] = 1

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    cnt = 0
    visit = [0 for i in range(1000000 + 1)]
    a = bfs(N,cnt)
    print('#%d %d' %(tc,a))
# def bfs(N,M):
#     global cnt
#     que = [N]
#     f= -1
#     visit[N] = 1
#     while que:
#         f +=1
#         N = que[f]
#         # x, cc = que.pop(0)
#         t = [N+1, N-1, N*2, N-10]
#         for i in range(len(t)):
#             if t[i] ==M:
#                 return visit[N]
#             if t[i]>0 and t[i] <=1000000:
#                 if visit[t[i]] == 0:
#                     visit[t[i]] = visit[N]+1
#                     que.append(t[i])
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int, input().split())
#     cnt = 0
#     visit = [0 for i in range(1000000 + 1)]
#     a = bfs(N,M)
#
#     print('#%d %d' %(tc,a))

