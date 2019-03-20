def isWall(x,y):
    if 0 <= y < 20:
        return True
    else:
        return False
def ladder(x,y):
    global result
    dy = [-1, 1]
    while data[x][y] !=2 :
        if isWall(x, y + dy[0]) and data[x][y + dy[0]] == 1:
            data[x][y] = 9
            y += dy[0]
        if isWall(x, y + dy[1]) and data[x][y + dy[1]] == 1:
            data[x][y] = 9
            y += dy[1]
        else:
            data[x][y] = 9
            x +=1
        if x==19:
            if data[x][y] == 2:
                return 1
            else:
                x = 0
                return data



import sys
sys.stdin = open("사다리(테스트).txt")
T = 1
for tc in range(1, T+1):
    N = int(input())
    result = 0
    data = [list(map(int, input().split())) for _ in range(20)]
    for i in range(len(data)):
        if data[0][i] == 1:
            result = ladder(0,i)
            # print(result)
            # if result ==1:
            #     print(i)
            #     break
        print(*data[i])