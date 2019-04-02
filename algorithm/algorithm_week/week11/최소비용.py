import sys
sys.stdin = open("최소비용.txt")
T = int(input())

for T in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    D = [[float('inf')]*N for _ in range(N)]
    D[0][0] = 0
    que = []
    que.append((0,0))
    dx = (0,0,-1,1)
    dy = (-1,1,0,0)
    while que:
        x,y = que.pop(0)
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N: continue
            diff = 0
            if data[nx][ny] > data[x][y]:
                diff = data[nx][ny] - data[x][y]
            if D[nx][ny] > (D[x][y] + diff + 1):
                D[nx][ny] = D[x][y] + diff + 1
                que.append((nx, ny))
    print('#%d %d' %(T,D[N-1][N-1]))
