import sys
sys.stdin = open('test_p2.txt')

T = int(input())
for tc in range(1,T+1):
    R,C = map(int, input().split())
    data = [list(map(int, input().split()))for _ in range(R)]
    a,b,c,d = 0,0,0,0
    for i in range(R):
        for j in range(C):
            hap1 = 0
            hap2 = 0
            for si in range(i,R-1):
                for sj in range(j, C - 1):
                    for ei in range(si+1,R):
                        hap1 += data[si][sj]
                        hap2 += data[ei][sj]
                        hap3,hap4 = 0,0
                        for ej in range(sj+1,C):
                            hap3+=data[si][ej]
                            hap4+=data[ei][ej]
                    print(hap1, end=" ")
                    print(hap2, end=" ")
                    print(hap3, end=" ")
                    print(hap4)
