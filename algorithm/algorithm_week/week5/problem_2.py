import sys
sys.stdin = open("problem_2.txt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data_total = [[0 for _ in range(N)] for _ in range(N)]
    data = []
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
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    re_a = a
    re_b = b # dx dy 카운트변수
    # while data_total[a][b] != 3:
    #     if data_total[a][b] == 2:
    #         for l in range(len(dx)):
    #             if data_total[a + dy[l]][b + dx[l]] == 0:
    #                 data_total[a][b] = 8  # 시작점 구분
    #                 a = a + dy[l]
    #                 b = b + dx[l]
    #                 break
    #     elif data_total[a][b] == 0:
    #         for l in range(len(dx)):
    #             if data_total[a + dy[l]][b + dx[l]] == 0:
    #                 data_total[a][b] = 9  # 방문
    #                 a = a + dy[l]
    #                 b = b + dx[l]
    #                 break
    #             if data_total[a + dy[l]][b + dx[l]] == 3:
    #                 data_total[a][b] = 9
    #                 a = a + dy[l]
    #                 b = b + dx[l]
    #                 break
    #         else:
    #             a, b = re_a, re_b
    #             l = 0
    #     for l in range(len(dx)):
    #         if data_total[a + dy[l]][b + dx[l]] == 0:
    #             data_total[a][b] = 9  # 방문
    #             a = a + dy[l]
    #             b = b + dx[l]
    #             break
    # if data_total[a][b] == 3:
    #     for z in range(len(dx)):
    #         if data_total[a + dy[z]][b + dx[z]] != 0:
    #             a = a + dy[z]
    #             b = b + dx[z]
    #         else:
    #             print("error")
    # print("1")


#########################3 튜터용
while data_total[a][b] != 3:
    if data_total[a][b] == 2:
        for l in range(len(dx)):
            if data_total[a + dy[l]][b + dx[l]] == 0 and a + dy[l]>=0 and b + dx[l] >=0:
                data_total[a][b] = 8  # 시작점 구분
                a = a + dy[l]
                b = b + dx[l]
                break
    elif data_total[a][b] == 0:
        for l in range(len(dx)):
            if data_total[a + dy[l]][b + dx[l]] == 0 and a + dy[l]>=0 and b + dx[l] >=0:
                data_total[a][b] = 9  # 방문
                a = a + dy[l]
                b = b + dx[l]
                break
            if data_total[a + dy[l]][b + dx[l]] == 3 and a + dy[l]>=0 and b + dx[l] >=0:
                data_total[a][b] = 9
                a = a + dy[l]
                b = b + dx[l]
                break
        else:
            a, b = re_a, re_b
            l = 0
    for l in range(len(dx)):
        if data_total[a + dy[l]][b + dx[l]] == 0 and a + dy[l]>=0 and b + dx[l] >=0:
            data_total[a][b] = 9  # 방문
            a = a + dy[l]
            b = b + dx[l]
            break
if data_total[a][b] == 3 and a + dy[l]>=0 and b + dx[l] >=0:
    for z in range(len(dx)):
        if data_total[a + dy[z]][b + dx[z]] != 0:
            a = a + dy[z]
            b = b + dx[z]
        else:
            print("error")
print("1")