#
# def find_road(a,b):
#     while
#
#     return
import sys
sys.stdin = open("미로탈출(중간).txt")

N = int(input())
data = [list(map(int,input())) for i in range(N)]
d = list(map(int, input().split()))
dno = 0
dr = [1,0,-1,0]
dc = [0,1,0,-1]
a,b = 1,1

for x in range(len(data)):
    data[x].append(1)
    data[x].insert(0,1)
data.append([1] * (N+2))
data.insert(0, [1] * (N+2))

while True:
    if data[a+dr[dno]][b+dc[dno]] == 0:
        data[a][b] = 9
        a = a+dr[dno]
        b = b+dc[dno]
    elif data[a+dr[dno]][b+dc[dno]] == 1:
        dno = (dno +1) % 4
    else:
        break




for x in range(len(data)):
    print(*data[x])


