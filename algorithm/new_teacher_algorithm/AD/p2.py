import sys
sys.stdin = open('p2.txt')

T = int(input())
for tc in range(1,T+1):
    R,C = map(int, input().split())
    data = [list(map(int, input().split()))for _ in range(R)]
    # print(R,C,data)

    for sr in range(R-1):
        hap1 = 0
        for sc in range(C-2):
            hap1 += data[sr][sc]
            hap3 = 0
            for mc in range(sc+1,C-1):
                hap3 +=data[sr][mc]
                hap5 = 0
                hap6 = 0
                hap4 = 0
                hap2 = 0
                for er in range(sr + 1, R):
                    hap4 += data[er][mc]
                    hap2 += data[er][sc]
                    for ec in range(mc + 1, C):
                        hap6 += data[er][ec]
                        hap5 += data[sr][ec]