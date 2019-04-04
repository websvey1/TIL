import sys
sys.stdin = open('자외선.txt')
def bfs(x,y):
    que = []
    dx = (0,0,-1,1)
    dy = (-1,1,0,0)
    que.append((x,y))
    while que:
        xx,yy = que.pop(0)
        # if xx == N-1 and yy==N-1: return
        for i in range(len(dx)):
            nx = xx+dx[i]
            ny = yy+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N: continue
            if visit[nx][ny] > visit[xx][yy]+data[nx][ny]:
                visit[nx][ny] = visit[xx][yy]+data[nx][ny]
                que.append((nx,ny))
    return visit[N-1][N-1]
N = int(input())
data = [list(map(int,input()))for _ in range(N)]
result = 0
visit = [[float('inf')]*N for _ in range(N)]
visit[0][0] = 0
a = bfs(0,0)
print(a)