# 미로 찾기

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
x,y = 0,0

for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if check