import sys, time
sys.stdin = open("./tc/hoimun.txt", "r")

start = time.time()
T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    data = [input() for _ in range(N)]
    sero = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            sero[j][i] = data[i][j]
    for i in range(N):
        sero[i] = "".join(sero[i])
    # ASD = "".join(sero[0])
    # print(sero)
    result = []
    for i in range(N):   # i는 행마다 도는거니까 이게 맞다
        for j in range(N-M+1):  # N-M에 +1한 이유 : 똑같을때도 1번은 돌아야함 // j는 0부터 7까지// k가 13개씩 돌꺼니까. 마지막항 19항까지 돌도록
            # if data[i][j:j+M] == data[i][j:j+M][::-1]:
            #     result = data[i][j:j+M]
            cnt = M//2  # 앞뒤 검사할꺼니까 길이 M의 반만 검사하면 됌
            for k in range(cnt):                 # k는
                if data[i][j+k] == data[i][M+j-(k+1)]:
                    cnt -=1
            if cnt == 0:
                # print("CHK")
                # print(k)
                result = data[i][j:M+j]
            # print(cnt)

    for i in range(N):
        for j in range(N - M + 1):
            # if sero[i][j:j+M] == sero[i][j:j+M][::-1]:
            #     result = sero[i][j:j+M]
            cnt = M // 2
            for k in range(cnt):
                if sero[i][j + k] == sero[i][M + j - (k + 1)]:
                    cnt -= 1
            if cnt == 0:
                # print("CHK")
                result = sero[i][j:M + j]
                # print(k)

    print("#%d %s" %(tc,result), time.time()-start)
        # print(data[i:i+(N-M+1)])
