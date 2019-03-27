def isWall(x,y):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    else:
        return True

def hunt(x,y):
    global cnt
    dx = [-1,-1,-1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1,-1, 1,-1, 0, 1]
    dno = 0
    home_x = x
    home_y = y
    while dno < len(dx) :
        x = x+dx[dno]
        y = y+dy[dno]
        if isWall(x,y):
            if data[x][y] ==3 or data[x][y]==1:
                x = home_x
                y = home_y
                dno +=1
            elif data[x][y] == 2:
                cnt +=1
                data[x][y] = 0
        else:
            x = home_x
            y = home_y
            dno +=1


import sys
sys.stdin = open("사냥꾼.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split()))for _ in range(N)]
    cnt = 0
    # print(data)
    for i in range(N):
        for j in range(N):
            if data[i][j]==1:
                hunt(i,j)
    print(cnt)