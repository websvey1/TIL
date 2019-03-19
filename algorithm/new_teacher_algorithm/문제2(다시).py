import sys
sys.stdin = open("문제2.txt")

def find_isd(x,y):
    global result
    stack.append(data[x][y])
    data[x][y] = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while stack:
        for i in range(len(dx)):
            if data[x+dx[i]][y+dy[i]] != 0:
                find_isd(x+dx[i], y+dy[i])
        break





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    result = 0
    RESULT = []
    MMAAXX = 0
    # print(data)



    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 0:
                find_isd(i,j)
                RESULT.append(stack)
                stack= []
    for i in range(len(RESULT)):
        if MMAAXX < max(RESULT[i]):
            MMAAXX = max(RESULT[i])
    print('#%d %d %d' %(tc, len(RESULT), MMAAXX))