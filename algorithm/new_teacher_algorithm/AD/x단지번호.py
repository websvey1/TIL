import sys
sys.stdin = open('단지번호.txt')

def dfs(x,y):
    global cnt
    # if x <0 or y<0 or x>=N or y >=N: return
    # if data[x][y] != 1: return
    data[x][y] = 0
    cnt +=1
    dx = (0,0,-1,1)
    dy = (-1,1,0,0)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N:continue
        if data[nx][ny]!=1: continue
        dfs(nx,ny)

N = int(input())
data = [list(map(int,input()))for _ in range(N)]
cnt_list = []

for i in range(N):
    for j in range(N):
        cnt = 0
        if data[i][j] == 1:
            dfs(i,j)
            cnt_list.append(cnt)
cnt_list.sort()
print(len(cnt_list))
for i in range(len(cnt_list)):
    print(cnt_list[i])