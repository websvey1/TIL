import sys
sys.stdin = open('p2.txt')

T = int(input())
for tc in range(1,T+1):
    R,C = map(int, input().split())
    data = [list(map(int, input().split()))for _ in range(R)]
    point = []
    comp = float('-inf')

    for i in range(R-1):
        for j in range(C-2):
            for k in range(j+1,C-1):
                point.append((i,j,k))
    # print(point)
    for i in range(len(point)):
        x,y1,y2 = point[i]
        sep_sum = [0] * 6
        for r in range(R):
            for c in range(C):
                if r<=x and c<=y1:
                    sep_sum[0] += data[r][c]
                if r>x and c <=y1:
                    sep_sum[1] += data[r][c]
                if r<=x and y1 < c <=y2:
                    sep_sum[2] += data[r][c]
                if r>x and y1 < c <= y2:
                    sep_sum[3] += data[r][c]
                if r<=x and c>y2:
                    sep_sum[4] += data[r][c]
                if r>x and c>y2:
                    sep_sum[5] += data[r][c]

        # print(sep_sum)
        for a in range(4):
            for b in range(a+1,5):
                for c in range(b+1,6):
                    hap = abs(sep_sum[a]-sep_sum[b])+ abs(sep_sum[b]-sep_sum[c])+abs(sep_sum[a]-sep_sum[c])
                    if hap > comp:
                        comp = hap
    print(comp)