import sys
sys.stdin = open("사냥꾼.txt")

def find_hunter(data):
    P = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 1:
                P.append([i,j])
            # else:
            #     return 0
    return P

def hunting(x,y):
    dx = [-1, 1, -1, 1, 1, 0, -1, 0]
    dy = [-1, 1, 1, -1, 0, -1, 0, 1]
    dno = 0
    global cnt
    home_x, home_y = x, y
    while dno < 8:
        x = x + dx[dno]
        y = y + dy[dno]
        if data[x][y] == 2:
            data[x][y] = 9
            cnt +=1
        elif data[x][y] == 0 or data[x][y]==1 :
            x = home_x
            y = home_y
            dno = dno+1
        elif data[x][y] == 9:
            data[x][y]  = 9
        else:
            break

    return data




N = int(input())
data = [[0] * (N+2) for _ in range(N+2)]
for i in range(1, N+1):
    data[i] = [0] + list(map(int, input())) + [0]
cnt = 0
a = find_hunter(data)
# print(a)
for i in range(len(a)):
    hunting(a[i][0],a[i][1])

print(cnt)

# for i in range(len(data)):
#     print(*data[i])