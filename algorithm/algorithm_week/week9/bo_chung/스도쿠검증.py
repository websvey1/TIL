def garo(data):
    global result
    list_garo = []
    for i in range(9):
        list_garo.append(data[i])

    if sorted(list_garo) != comp:
        result = 1
    # print(list_garo)
def sero(data):
    global result

    for i in range(9):
        list_sero = []
        for j in range(9):
            list_sero.append(data[j][i])
        if sorted(list_sero) != comp:
            result = 1
        # print(list_sero)

def square(i,j):
    global result
    list_square = []
    for x in range(3):
        for y in range(3):
            list_square.append(data[x][y])
    if sorted(list_square) != comp:
        result = 1


import sys
sys.stdin = open("스도쿠검증.txt")

T = int(input())
for tc in range(1,T+1):
    data = [list(map(int, input().split())) for _ in range(9)]
    comp = [1,2,3,4,5,6,7,8,9]
    result = 0

    for i in range(len(data)):
        garo(data[i])
        for j in range(len(data[i])):
            if i==j and i %3 ==0 or j%3 == 0:
                square(i,j)
            if i==0:
                sero(data)
    if result:
        print('#%d %d' %(tc, 0))
    else:
        print('#%d %d' %(tc, 1))

