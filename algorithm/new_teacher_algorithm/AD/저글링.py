import sys
sys.stdin = open('저글링.txt')
def BFS():
    global cnt
    que = []
    dy = (-1,1,0,0)
    dx = (0,0,-1,1)
    que.append((ir, ic, cnt))
    data[ir][ic] = 0
    while que:
        r,c,cnt = que.pop(0)
        for i in range(4):
            nr = r+dx[i]
            nc = c+dy[i]
            if nr<0 or nc<0 or nr>R or nc >C: continue
            if data[nr][nc] != 1: continue
            que.append((nr,nc,cnt+1))
            data[nr][nc] = 0

    return cnt


C,R = map(int, input().split())
data = [list(map(int, input()))for _ in range(R)]

ic, ir = map(int, input().split())
CNT = 0
cnt = 0
# 벽씌욱
for i in range(len(data)):
    data[i].append(0)
    data[i].insert(0, 0)
data.append([0]*(C+2))
data.insert(0, [0]*(C+2))
a = BFS()
for i in range(R+2):
    for j in range(C+2):
        if data[i][j] == 1:
            CNT +=1
print(a+3)
print(CNT)