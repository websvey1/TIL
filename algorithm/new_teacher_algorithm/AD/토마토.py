import sys
sys.stdin = open('토마토.txt')
def BFS():
    que = []
    dx = (0,0,-1,1)
    dy = (-1,1,0,0)
    start = []
    cnt = 0
    c = 0
    for i in range(C):
        for j in range(R):
            if data[i][j] == 1: # 익은 토마토자리를 모두 시작점으로 큐에 저장
                que.append((i, j,0))
            elif data[i][j] == 0: cnt +=1
    if cnt == 0: return 0 # 모두 익혀져 있는것
    while que:
        xx,yy,c = que.pop(0)
        for i in range(4):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if nx <0 or ny<0 or nx>=C or ny >=R: continue
            if data[nx][ny] ==0:
                que.append((nx,ny,c+1))
                data[nx][ny] = 1
                cnt -=1
    if cnt : return -1
    else: return c
R,C = map(int, input().split())
data = [list(map(int,input().split()))for _ in range(C)]
a = 0

a = BFS()
print(a)
