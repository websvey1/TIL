import sys
sys.stdin = open('로봇.txt')
def bfs():
    dr = (0,0,0,1,-1)
    dc = (0,1,-1,0,0)
    turn =  [(0,0),(4,3),(3,4),(1,2),(2,1)] #동서남북 행 = 열 =
    que = []
    que.append((sr,sc,sd,0))
    arr[sd][sr][sc] = 1
    while que:
        x,y,d,cnt = que.pop(0)
        if x==er and y==ec and d==ed: return cnt
        for i in range(1,4): # go 1,2,3
            nx = x+dr[d]*i
            ny = y+dc[d]*i

            if nx<0 or ny<0 or nx>=R or ny>=C: break
            if arr[d][nx][ny]: continue
            if data[nx][ny]:break
            que.append((nx,ny,d,cnt+1))
            arr[d][nx][ny] = 1

        for i in range(2): #turn left, right
            if arr[turn[d][i]][x][y]: continue
            que.append((x,y,turn[d][i],cnt+1))
            arr[turn[d][i]][x][y] = 1
R,C = map(int, input().split())
data = [list(map(int, input().split()))for _ in range(R)]
arr = [[[0]*C for i in range(R)]for j in range(5)]
# print(arr)
sr,sc,sd = map(int, input().split())
er,ec,ed = map(int, input().split())
sr-=1; sc-=1
er-=1; ec-=1
result = bfs()
print(result)