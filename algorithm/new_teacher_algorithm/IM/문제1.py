def hap():
    global data, N, K, tc
    MMIINN = 99999
    for k in range(N-K+1):
        for L in range(N-K+1):
            dagag_1 = 0
            dagag_2 = 0
            for i in range(N-K+2):
                for j in range(N-K+2):
                    if i+k == j+L:
                        dagag_1 += data[i+k][j+L]
                    if i+j == N-K+1:
                        dagag_2 += data[i+k][j+L]
            if MMIINN > abs(dagag_1-dagag_2):
                MMIINN = abs(dagag_1-dagag_2)
    print('#%d %d' %(tc,MMIINN))


import sys
sys.stdin = open("문제1.txt")

T= int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    hap()


