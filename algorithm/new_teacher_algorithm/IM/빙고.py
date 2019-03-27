def find(t):
    for i in range(N):
        for j in range(N):
            if t in data[i]:
                data[i][data[i].index(t)] =0
                return data

def isbingo():
    sero = 0
    dagag = 0
    dagag_2 = 0
    BBBBB = 0

    for i in range(N):
        for j in range(N):
            if 0 in data[i]:
                if sum(data[i]) == 0:  # 이게 못잡나??????
                    BBBBB +=1
                    break
                else:
                    break

    for j in range(N):
        for i in range(N):
            if data[i][j] !=0:
                break
            else:
                sero +=1
        if sero == N:
            BBBBB +=1
            sero = 0
            # break  # 이 뒤에 세로 빙고가 더 있을수 있는데 break를 해버림. continue로 바꿀것
        else:
            sero = 0


    for i in range(N):
        for j in range(N):
            if i == j:
                if data[i][j] == 0:
                    dagag +=1
                else:
                    dagag = 0
    if dagag == N:
        BBBBB+=1


    for i in range(N):
        for j in range(N):
            if i+j == N-1:
                if data[i][j] == 0:
                    dagag_2 +=1
    if dagag_2 == N:
        BBBBB +=1
    else:
        dagag_2 = 0

    return BBBBB



import sys
sys.stdin = open("빙고.txt")

N = 5
data = [list(map(int, input().split())) for i in range(N)]
answer = [list(map(int, input().split())) for i in range(N)]
cnt=0
ANS = 0
# for i in range(N):
    # print(*data[i])

# for i in range(N):
    # print(*answer[i])

for i in range(N):
    for j in range(N):
        find(answer[i][j])
        cnt +=1
        if cnt >11:
            if isbingo() >= 3:
                ANS = 1
                print(cnt)
                break
        #     if ANS == 1:
        #         break
        # if ANS == 1:
        #     break
    if ANS == 1:
        break




