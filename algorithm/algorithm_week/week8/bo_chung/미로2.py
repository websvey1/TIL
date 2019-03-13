def findstart():
    for i in range(100):
        if 2 in data[i]:
            return i, data[i].index(2)

def bfs(x,y):
    global Q, visit, result
    Q.append((x,y))
    while len(Q) != 0:
        x,y = Q.pop(0)
        # visit[x][y] = 1
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        for i in range(len(dx)):
            if x + dx[i] <0 or x+dx[i]>len(data) or y + dy[i] <0 or y+dy[i] >len(data):
                continue
            if data[x+dx[i]][y+dy[i]] == 0 and visit[x+dx[i]][y+dy[i]] !=1:
                Q.append((x+dx[i],y+dy[i]))
                visit[x+dx[i]][y+dy[i]] = 1
            if data[x+dx[i]][y+dy[i]] == 1:
                continue
            if data[x+dx[i]][y+dy[i]] == 3:
                result = 1
                return



import sys
sys.stdin = open("미로2.txt")

T = 10
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(100)]
    visit = [[0 for _ in range(100)] for _ in range(100)]
    x,y =findstart()
    Q = []
    result = 0
    bfs(x,y)
    print("#%d %d" %(tc, result))