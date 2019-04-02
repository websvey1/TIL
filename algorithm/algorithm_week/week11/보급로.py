import sys
sys.stdin = open('보급로.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input()))for _ in range(N)]
    D = [[float('inf')]*N for _ in range(N)]
    D[0][0] = 0
    dx = (0,0,-1,1)
    dy = (-1,1,0,0)
    que = [(0,0)]
    cnt = 0
    while que:
        x,y = que.pop(0)
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N:continue
            # if data[nx][ny] > data[x][y]:
            #     D[nx][ny] = data[nx][ny]
            if D[nx][ny] > D[x][y]+data[nx][ny]:
                D[nx][ny] = D[x][y]+data[nx][ny]
                que.append((nx,ny))
    print('#%d %d' %(tc,D[N-1][N-1]))
    # print(cnt)
    # print(D)
