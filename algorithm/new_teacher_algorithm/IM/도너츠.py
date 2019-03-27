import sys
sys.stdin = open("도너츠.txt")

N,K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
# print(data)a
max_hap = 0
for i in range(N-K+1):
    for j in range(N-K+1):
        hap = 0
        for k in range(K):
            for L in range(K):
                if k==0 or L==0 or k==K-1 or L==K-1:
                    hap += data[i+k][j+L]
        if hap > max_hap:
            max_hap =  hap
print(max_hap)