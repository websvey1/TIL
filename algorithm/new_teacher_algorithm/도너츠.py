import sys
sys.stdin = open("도너츠.txt")
N,K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
print(data)
for i in range(N-K+1):
    for j in range(N-K+1):
        hap = 0
        for k in range(K):
            for L in range(K):
                hap += data[i+k][j+L]

        print(hap)