import sys
sys.stdin = open('samsung1.txt')
def down(copy_data):
    temp = copy_data[:]
    for i in range(R):
        if i != R-1:
            temp[i+1] = copy_data[i]
        else:
            temp[R-(1+i)] = copy_data[i]
    return temp

def bfs():
    print(11)
    global result, arrow_list
    copy_data = data
    CCNNTT = 0
    q = []
    visit = [[0 for _ in range(C)] for _ in range(R)]
    dx = (0, 0, -1)
    dy = (-1, 1, 0)
    for i in range(R):
        for j in range(C):
            if copy_data[i][j] ==9:
                q.append((R-1,j,1))

                while q:
                    x,y,cc = q.pop(0)
                    for DI in range(len(dx)):
                        nx = x+dx[DI]
                        ny = y+dy[DI]
                        if nx<0 or ny<0 or nx>=R or ny>=C: continue
                        if visit[nx][ny]==1: continue
                        if cc==D:
                            copy_data = down(copy_data)
                        if cc>D: return
                        if copy_data[nx][ny] == 1:
                            CCNNTT +=1
                            copy_data[nx][ny] = 0
                            print(arrow_list, cc ,CCNNTT)
                        q.append((nx,ny,cc+1))
                        visit[nx][ny] = 1

def arrow(x,n,k):
    global arrow_list
    if k == 3:
        arrow_list.append(chk[:])
        # bfs(chk)
        # print(arrow_list)
        return
    if x>=n: return
    else:
        chk[x] = 9
        arrow(x+1,n,k+1)
        chk[x] = 0
        arrow(x+1,n,k)

R,C,D = map(int,input().split())
data = [list(map(int, input().split()))for _ in range(R)]
result = float('inf')
chk = [0]*C
arrow_list = []

arrow(0,C,0)
# print(arrow_list)
bfs()