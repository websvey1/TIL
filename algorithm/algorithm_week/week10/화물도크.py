import sys
sys.stdin = open("화물도크.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = sorted([list(map(int, input().split())) for _ in range(N)])
    time = [0 for _ in range(25)]
    cnt = 0
    dif_list = [0 for _ in range(N)]
    dif_table = [0 for _ in range(N)]
    for i in range(N):
        dif_table[i] = [data[i][1] - data[i][0],i]
    dif_table = sorted(dif_table)
    # print(dif_table)
    for i in range(len(dif_table)):
        dif_list[i] = dif_table[i][1]
    print(dif_list)
    print(data)

    for i in range(len(dif_list)):
        for j in range(data[dif_list[i]][0],data[dif_list[i]][1],1):
            if time[j] == 0:
                time[j] = 1
                if j == data[dif_list[i]][1]-1:
                    cnt += 1


            else:
                break
    print('#%d %d' %(tc,cnt))