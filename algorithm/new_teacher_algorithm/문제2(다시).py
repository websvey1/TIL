import sys
sys.stdin = open("문제2.txt")

def start(a):
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                return i,j
T = int(input())
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
# print(data)

x,y = start(data)
dx = [0,0,-1,1]
dy = [-1,1,0,0]

isd = 0
for i in range(x,N):
    for j in range(y,N):
        cnt = 0
        if data[i][j] != 0:
            for k in range(len(dx)):
                if data[i+dx[k]][j+dy[k]] == 0:
                    cnt +=1
                else:
                    data[i][j] = 0
                    break
            if cnt == 4:
                data[i][j] = 0
                isd +=1
print(isd)
    # print(*data[i])