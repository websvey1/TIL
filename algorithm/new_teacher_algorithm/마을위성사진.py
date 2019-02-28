import sys
sys.stdin = open("마을위성사진.txt")

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
cnt = 0
maxi = 1
a = 0
# print(data)
while cnt <= maxi:
    cnt += 1
    for i in range(1, N-1):
        for j in range(1, N-1):
            if data[i][j] != 0:
                ept_list = []
                if data[i-1][j] != 0 and data[i+1][j] != 0 and data[i][j-1] != 0 and data[i][j+1] != 0:
                    ept_list.append(data[i-1][j])
                    ept_list.append(data[i+1][j])
                    ept_list.append(data[i][j-1])
                    ept_list.append(data[i][j+1])
                    # print(min(ept_list))
                    data[i][j] = min(ept_list) + 1
                    if data[i][j] > maxi:
                        maxi = data[i][j]
    for i in range(N):
        for j in range(N):
            if a < data[i][j]:
                a = data[i][j]

print(a)