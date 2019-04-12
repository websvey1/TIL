import sys
sys.stdin = open('p1.txt')

def rab(data):
    # 0 위 1 아래 2 왼쪽 3 오른쪽
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    Q = [(data[0], data[1])]
    n = data[3]
    chk[data[0]][data[1]] += 1
    while Q:
        x, y = Q.pop(0)
        rex = x + (dx[data[2]] * n)
        rey = y + (dy[data[2]] * n)
        if 0 <= rex <= M-1 and 0 <= rey <= N-1:
            chk[rex][rey] += 1
            Q.append((rex, rey))

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    chk = [[0]*N for _ in range(M)]
    maxn = -1
    cnt = 0

    for i in range(len(arr)):
        rab(arr[i])

    for i in range(M):
        for j in range(N):
            if chk[i][j] > maxn:
                maxn = chk[i][j]

    for i in range(M):
        for j in range(N):
            if chk[i][j] == maxn:
                cnt += 1

    print('#{} {} {}'.format(tc+1, maxn, cnt))