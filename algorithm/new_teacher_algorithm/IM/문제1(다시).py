import sys
sys.stdin = open("문제1.txt")

T = int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    # print(N,K)
    data = [list(map(int, input().split()))for _ in range(N)]
    result = 99999999999999999999
    for i in range(N-K+1):
        for j in range(N-K+1):
            dgs_1 = 0
            dgs_2 = 0
            for k in range(K):
                for L in range(K):
                    if k==L:
                        dgs_1 +=data[i+k][j+L]
                    if k+L == K-1:
                        dgs_2 += data[i+k][j+L]
            if result > abs(dgs_1-dgs_2):
                result = abs(dgs_1-dgs_2)
    print('#%d'%(tc), result)