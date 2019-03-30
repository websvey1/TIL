import sys
sys.stdin = open('토마토.txt')

def bfs():
    global que, cnt
    dx = (0,0,-1,1)
    dy = (-1,1,0,0)
    while que:
        xx,yy,cc = que.pop(0)
        for i in range(len(dx)):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if nx <0 or ny < 0 or nx>=R or ny>=C: continue
            if data[nx][ny]==1:continue
            if data[nx][ny]==-1:continue
            data[nx][ny] = 1
            que.append((nx,ny,cc+1))
    for c in range(R):
        if 0 in data[c]:
            return -1
        return cc

C,R = map(int, input().split())
data = [list(map(int, input().split()))for _ in range(R)]
# print(data)
que = []
cnt = 0
for i in range(R):
    for j in range(C):
        if data[i][j] == 1:
            que.append((i,j,cnt))
# print(que)
a = bfs()
print(a)
