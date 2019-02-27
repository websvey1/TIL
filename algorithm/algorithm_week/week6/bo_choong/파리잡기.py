import sys
sys.stdin = open("파리잡기.txt")

def get_sum(i,j):
    global M
    hap = 0
    for k in range(M):
        for L in range(M):
            hap += data[i + k][j + L]
    return hap

T = int(input())
for tc in range(1, T+1):

    result = 0
    N,M = map(int, input().split())
    # print(N,M)
    data = [list(map(int, input().split())) for _ in range(N)]
    # print(data)
    for i in range(len(data)-(M-1)): #   N-M+1 == len(data)-(M-1)
        for j in range(len(data[i])-(M-1)):
            # hap = 0
            # for k in range(M):
            #     for L in range(M):
            #         hap += data[i+k][j+L]
            hap = get_sum(i,j)
            if hap > result:
                result = hap
            else:
                continue
    # print(f'#{tc} {result})
    print("#%d %d" % (tc, result))