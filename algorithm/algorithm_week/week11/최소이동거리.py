import sys
sys.stdin = open('최소이동거리.txt')

T = int(input())
for tc in range(1,T+1):
    N,E = map(int, input().split())
    data = [list(map(int, input().split()))for _ in range(E)]

    arr = [[0] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        arr[data[i][0]][data[i][1]] = data[i][2]

    D = [float('inf') for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    cnt = 0
    D[cnt] = 0


    while cnt<N:
        visited[cnt] = 1
        for i in range(len(data)):
            p1 = data[i][0]
            p2 = data[i][1]
            if p1 == cnt and visited[p2]==0:
                D[p2] = min(D[p2], D[cnt]+arr[p1][p2])
        result = float('inf')
        for j in range(len(D)):
            if visited[j] == 0 and D[j] < result:
                result = D[j]
                cnt = j
    print(D)
    print('#%d %d' %(tc,D[-1]))
