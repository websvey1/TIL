import sys
sys.stdin = open('samsung1.txt')
def bfs(chk):
    global result
    copy_data = data
    CCNNTT = 0
    q = []
    visit = [[0 for _ in range(C)] for _ in range(R)]
    dx = (0, 0, -1)
    dy = (-1, 1, 0)
    for j in range(C):
        if chk[j] ==9:
            # visit[R-1][j] = 1
            q.append((R-1,j,1))

    while q:
        x,y,cc = q.pop(0)
        for DI in range(len(dx)):
            nx = x+dx[DI]
            ny = y+dy[DI]
            if nx<0 or ny<0 or nx>=R or ny>=C: continue
            if visit[nx][ny]==1: continue
            if cc>D: return
            if copy_data[nx][ny] == 1:
                CCNNTT +=1
                copy_data[nx][ny] = 0
                print(chk, cc ,CCNNTT)
            q.append((nx,ny,cc+1))
            visit[nx][ny] = 1



def arrow(x,n,k):
    global arrow_list
    if x == k:
        cnt = 0
        for Z in range(C):
            if chk[Z]==9: cnt +=1
        if cnt==3:
            # arrow_list.append(chk) # 왜 여기 안들어가지?
            bfs(chk)
            # print(chk)
        return
    else:
        for i in range(x,n):
            if chk[i]:continue
            chk[i] = 9
            arrow(x+1,n,k)
            chk[i] = 0
R,C,D = map(int,input().split())
data = [list(map(int, input().split()))for _ in range(R)]
# print(R,C,D,data)
result = 0
chk = [0]*C
arrow_list = []
data.append([0]*C)
# print(data)
arrow(0,C,3)
print(arrow_list)