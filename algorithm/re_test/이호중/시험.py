import sys
sys.stdin = open('p1.txt')
def bfs():
    que = []
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)
    for i in range(len(data)):
        que.append((data[i][0],data[i][1],data[i][2],data[i][3]))
        chk[data[i][0]][data[i][1]] +=1
    while que:
        x,y,dir,jump = que.pop(0)
        nx = x+(dx[dir]*jump)
        ny = y+(dy[dir]*jump)
        if nx<0 or ny<0 or nx>=N or ny>=N: continue
        chk[nx][ny] +=1
        que.append((nx,ny,dir,jump))
T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    chk = [[0]*N for _ in range(N)]
    # print(data)
    SS,MM = 0,0
    bfs()
    # print(chk)
    for K in range(len(chk)):
        SS = max(SS,max(chk[K]))
    # print(SS)
    for L in range(len(chk)):
        MM += chk[L].count(SS)
    print('#%d %d %d' %(tc,SS,MM))