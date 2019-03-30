import sys
sys.stdin = open('p2.txt')

T = int(input())
for tc in range(1,T+1):
    R,C = map(int, input().split())
    data = [list(map(int, input().split()))for _ in range(R)]
    # print(R,C,data)
    for i in range(R-1):
        for j in range(i+1,R):
            for ci in range(C-2):
                for cj in range(ci+1,C-1):
                    for ck in range(cj+1,C):
