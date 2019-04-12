import sys
sys.stdin = open('p2.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxn = -1

    for i in range(1, N):
        for j in range(1, M):
            a = []
            s1, s2, s3, s4 = 0, 0, 0, 0
            # 1
            for y in range(i):
                for x in range(j):
                    s1 += arr[y][x]
            # 2
            for y in range(i):
                for x in range(j, M):
                    s2 += arr[y][x]
            # 3
            for y in range(i, N):
                for x in range(j):
                    s3 += arr[y][x]
            # 4
            for y in range(i, N):
                for x in range(j, M):
                    s4 += arr[y][x]
            a.append(sorted([s1, s2, s3, s4]))

            b = abs(a[0][0] - a[0][-1])
            if b > maxn:
                maxn = b

    print('#{} {}'.format(tc+1, maxn))