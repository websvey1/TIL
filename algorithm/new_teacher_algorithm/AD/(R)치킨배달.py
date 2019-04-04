import sys
sys.stdin = open('치킨배달.txt')
def hap():
    HAP = 0
    for i in range(len(point_h)):
        MMIINN = 20*20
        for j in range(len(point_c)):
            if not a[j]:continue
            MMIINN = min(MMIINN, data[j][i])
        HAP += MMIINN
    return HAP

def dfs(x,n,cnt):
    global result
    if cnt==n:
        HAP = hap()
        if result > HAP:
            result = HAP
        return

    if x>=len(point_c):return
    a[x] = 1
    # print(a)
    dfs(x+1,n,cnt+1)
    a[x] = 0
    dfs(x + 1, n, cnt)
N,M = map(int,input().split())
city = [list(map(int, input().split()))for _ in range(N)]
point_c = []
point_h = []
result = float('inf')
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            point_h.append((i,j))
        if city[i][j] == 2:
            point_c.append((i, j))
# print(point_c)
# print(point_h)
data = [[0]*len(point_h) for _ in range(len(point_c))]
for i in range(len(point_c)):
    for j in range(len(point_h)):
        data[i][j] = abs(point_h[j][0]-point_c[i][0]) + abs(point_h[j][1]-point_c[i][1])
# for i in range(len(point_c)):
#     print(*data[i])
a = [0]*len(point_c) #  고른치킨집
dfs(0,M,0) #0행(첫번째치킨부터), 개수는 0개로 시작
print(result)