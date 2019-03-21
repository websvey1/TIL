import sys
sys.stdin = open("단어자리.txt")

T = int(input())
for tc in range(1, T+1):
    N,K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    sero_data = [[0 for _ in range(N)]for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] ==1 and visited[i][j] ==0:
                cnt = 0
                k=j
                while k < N and data[i][k] ==1:
                    cnt +=1
                    visited[i][k] = 1
                    k += 1
                if cnt == K:
                    result +=1

    for i in range(N):
        for j in range(N):
            sero_data[i][j] = data[j][i]

    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if sero_data[i][j] ==1 and visited[i][j] ==0:
                cnt = 0
                k=j
                while k < N and sero_data[i][k] ==1:
                    cnt +=1
                    visited[i][k] = 1
                    k += 1
                if cnt == K:
                    result +=1
    print('#%d %d' %(tc,result))

