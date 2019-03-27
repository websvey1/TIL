def islake(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for D in range(1, N):
        for j in range(4):
            if data[x+dx[j]*D][y+dy[j]*D] ==0:
                data[x][y] = D
                return data



import sys
sys.stdin = open("호수의깊이.txt")

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
hap = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            islake(i, j)

for i in range(N):
    for j in range(N):
        hap += data[i][j]
print(hap)
# for k in range(N):
#     print(*data[k])




