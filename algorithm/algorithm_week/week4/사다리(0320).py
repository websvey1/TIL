def isWall(x,y):
    if 0 <= y < 100:
        return True
    else:
        return False
def ladder(x,y):
    global result
    dy = [-1, 1]
    while x < 100:
        if isWall(x, y + dy[0]) and data[x][y + dy[0]] == 1:
            # data[x][y] = 9
            while True:
                y += dy[0]
                if data[x+1][y] == 1:
                    break
            x += 1
        elif isWall(x, y + dy[1]) and data[x][y + dy[1]] == 1:
            # data[x][y] = 9
            while True:
                y += dy[1]
                if data[x+1][y] == 1:
                    break
            x += 1
        else:
            x += 1

        if x==99:
            if data[x][y] == 2:
                return 1




import sys
sys.stdin = open("사다리.txt")
T = 10
for tc in range(1, T+1):
    N = int(input())
    result = 0
    data = [list(map(int, input().split())) for _ in range(100)]
    for i in range(len(data)):
        if data[0][i] == 1:
            result = ladder(0,i)
            # print(result)
            if result ==1:
                print('#%d %d' %(tc,i))
        # print(*data[i])
    # print(result)