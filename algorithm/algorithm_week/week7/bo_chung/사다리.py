def iswall(data):
    for i in range(len(data)):
        data[i].append(0)
        data[i].insert(0,0)
    data.append([0] * (len(data)+2))
    data.insert(0, [0]*(len(data)+2))
    return data

def find_road(data):
    dx = [1,0,0]
    dy = [0, -1, 1]
    dno = 0
    x,y = 1,1
    while data[x][y] !=2:
        if data[x][y] == 1:           # 현재위치가 1이면
            x = x+dx[dno]               #우선 아래로이동
            y = y+dy[dno]

        elif data[x][y] ==0:
            dno +=1









import sys
sys.stdin = open("사다리.txt")

T = 10
for i in range(1, T+1):
    tc = int(input())
    data = [list(map(int, input().split())) for i in range(100)]
    iswall(data)
    print(data)
    find_road(data)