import sys
sys.stdin = open('p2.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(N,M,data)
    result = 0
    point = []
    for i in range(1,N):
        for j in range(1,M):
            point.append((i,j))
    # print(point)

    for k in range(len(point)):
        x,y = point[k]
        hap1, hap2, hap3, hap4 = 0, 0, 0, 0
        for i in range(N):
            for j in range(M):
                if i<x and j<y:
                    hap1 +=data[i][j]
                elif i<x and j>=y:
                    hap2 += data[i][j]
                elif i>=x and j<y:
                    hap3 += data[i][j]
                elif i>=x and j>=y:
                    hap4 += data[i][j]
        middle = abs(max(hap1,hap2,hap3,hap4)-min(hap1,hap2,hap3,hap4))
        result = max(result,middle)
    print('#%d %d' %(tc,result))