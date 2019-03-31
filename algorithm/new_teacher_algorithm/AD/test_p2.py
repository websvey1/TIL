import sys
sys.stdin = open('test_p2.txt')
def dfs(n,cnt):
    global result
    if n >=len(comp):
        print(result)
        return
    result[n] = comp[n]
    dfs(n+1, cnt+1)
    result[n] = 0
    dfs(n+1, cnt)


T = int(input())
for tc in range(1,T+1):
    R,C = map(int, input().split())
    data = [list(map(int, input().split()))for _ in range(R)]
    cnt = 0
    hap1 = 0
    hap2 = 0
    result = [0 for _ in range(10)]
    for si in range(R-1):
        for sj in range(C - 1):
            hap3, hap4 = 0, 0
            comp = []
            for ei in range(si+1,R):
                hap1 += data[si][sj]
                hap2 += data[ei][sj]
                for ej in range(sj+1,C):
                    hap3 += data[si][ej]
                    hap4 += data[ei][ej]
                comp.append(hap3)
                comp.append(hap4)
            comp.append(hap1)
            comp.append(hap2)
            # print(hap1, end=" ")
            # print(hap2, end=" ")
            # print(hap3, end=" ")
            # print(hap4)
            print(comp)
            dfs(0,cnt)
