import sys
sys.stdin = open('미로탈출.txt')
def bfs():
    global bomb
    que = []
    que.append((sx,sy,bomb,0))
    dx = (0,0,-1,1)
    dy = (-1,1,0,0)
    # chk[bomb][sx][sy] =9
    while que:
        x,y,b,hap = que.pop(0)
        if x==ex and y==ey: return hap
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=R or ny>=C: continue
            if data[nx][ny] ==1: continue
            if chk[b][nx][ny] == 9: continue
            if data[nx][ny] == 2:
                if b:
                    que.append((nx,ny,b-1,hap+1))
                    chk[b-1][nx][ny] = 9
                else:
                    continue
            else:
                que.append((nx,ny,b,hap+1))
                chk[b][nx][ny] = 9
R,C = map(int, input().split())
data = [list(map(int, input().split()))for _ in range(R)]
chk = [[[0 for _ in range(C)]for _ in range(R)] for _ in range(4)]
for i in range(R):
    for j in range(C):
        if data[i][j] ==3:
            sx,sy = i,j
        if data[i][j] ==4:
            ex, ey = i,j
bomb = 3
a = bfs()
if a:
    print(a)
else:
    print(-1)