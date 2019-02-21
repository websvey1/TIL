import sys
sys.stdin = open("problem_2.txt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data_total = [[0 for _ in range(N)] for _ in range(N)]
    # data_total = [list(map(int, input())) for i in range(N)]

    data = []
    miro = []
    result = 0
    a,b = 0,0
    for i in range(N):
        data.extend(list(map(str, input().split())))
    # print(data)
    for j in range(N):
        for k in range(N):
            data_total[j][k] = int(data[j][k])
    print(data_total)
    for l in range(len(data_total)):
        if 2 in data_total[l]:
            a, b = l, data_total[l].index(2)
    # print(a,b)
    a +=1
    if data_total[a][b] == 0:
        a += 1
        if data

