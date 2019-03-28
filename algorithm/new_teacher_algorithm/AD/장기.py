import sys
sys.stdin = open("장기.txt")
def BFS(x,y,c):
    dx = (-1, 1,-2,-2,-1, 1, 2, 2)
    dy = (-2,-2,-1, 1, 2, 2,-1, 1)
    que = []
    que.append((x,y,c))
    while que:
        xx,yy,cc = que.pop(0)
        for i in range(len(dx)):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if nx <0 or ny<0 or nx>=N or ny >=M: continue # 왜 N, M이지?...
            # if nx != S or ny !=K: continue
            if visit[nx][ny] == 1: continue
            if nx==S and ny==K: return cc+1
            visit[nx][ny] = 1
            que.append((nx,ny,cc+1))
    return -1




N,M = map(int, input().split())
R,C,S,K = map(int, input().split())
N -=1;M-=1;R-=1;C-=1;S-=1;K-=1
visit = [[0 for _ in range(M)]for _ in range(N)]
# print(N,M,R,C,S,K)
cnt = 0
aa = BFS(R,C,cnt)
print(aa)
