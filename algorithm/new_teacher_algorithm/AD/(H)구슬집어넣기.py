import sys
sys.stdin = open('구슬집어넣기.txt')
def bfs():
    que = []
    dx = (0,0,-1,1)
    dy = (-1,1,0,0)
    que.append((rsx,rsy,bsx,bsy,0))
    chk[rsx][rsy][bsx][bsy] = 1

T = int(input())
for tc in range(1,T+1):
    R,C = map(int, input().split())
    data = [list(input()) for _ in range(R)]
    chk = [[[[0]*C for _ in range(R)] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if data[i][j] =='R':
                rsx, rsy = i,j
            if data[i][j] =='B':
                bsx, bsy = i,j
            if data[i][j] =='H':
                hx,hy = i,j
    bfs()
