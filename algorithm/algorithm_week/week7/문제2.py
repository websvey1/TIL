def find_island(x,y):
    dx = [0,1]
    dy = [1,0]
    check_x , check_y = 0,0
    cnt =0
    island = 0
    for i in range(x,N-1):
        for j in range(y,N-1):
            if data[i][j] != 0:
                check_x = i
                check_y = j
                if data[i+dx[0]][j+dy[0]] == 0 and data[i+dx[1]][j+dy[1]] == 0 and cnt>N-1:
                    print(1)
                return i, j
            else:
                cnt +=1


    # return island

def max_height():
    max_value = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] >max_value:
                max_value = data[i][j]
    return max_value



# import sys
# sys.stdin = open("문제2.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for i in range(N)]
    MAX_HEIGHT = 0
    ISLAND = 0
    # print(data)
    MAX_HEIGHT= max_height()
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                ISLAND = find_island(i,j)
                if ISLAND != 0:
                    ISLAND =2  # 출력만 되게 했음
    print(ISLAND)

    print('#%d %d %d' %(tc, ISLAND, MAX_HEIGHT))

