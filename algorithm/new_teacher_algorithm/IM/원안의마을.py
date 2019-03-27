def find_LTE(n):
    for i in range(N):
            if 2 in data[i]:
                # data[i][data[i].index(2)] = 0
                return i, data[i].index(2)

def find_long():
    a,b = find_LTE(data)
    M = 0
    for i in range(N):
        for j in range(N):
            if data[i][j]==1:
                x = i
                y = j
                if M < (x-a)**2+(y-b)**2:
                    M = (x-a)**2+(y-b)**2

    return M
import sys
sys.stdin = open("원안의마을.txt")

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
# print(data)
A = find_long()
for k in range(14):

    if (k**2) >= A:
        print(k)
        break
# for i in range(N):
#     print(*data[i])