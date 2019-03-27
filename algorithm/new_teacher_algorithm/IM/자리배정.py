import sys
sys.stdin = open("자리배정.txt")


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(C,R,target):
    data = [[0 for _ in range(C)] for _ in range(R)]
    cnt = 0
    i = j = 0
    flag = 0 # 방향전환변수 상하/좌우
    while cnt <= C*R:
        cnt +=1
        if cnt == target:
            print(data)
            return j+1, i+1
        data[i][j] = cnt
        if flag %2 == 0:
            i += dy[flag]
            if i + dy[flag] < 0 or i + dy[flag] >=R or data[i+dy[flag]][j]:
                flag = (flag +1) %4
        elif flag %2 ==1:
            j +=dx[flag]
            if j + dx[flag] < 0 or j+dx[flag] >= C or data[i][j+dx[flag]]:
                flag = (flag + 1) %4
    return 0


C,R = map(int, input().split())
target = int(input())
answer = solution(C,R,target)

if answer:
    print(*answer)
else:
    print(0)






for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            data[i][j] = cnt
            cnt +=1
    if j == len(data[i])-1:
        for i in range(len(data)):
            if data[i][j] ==0:
                data[i][j] = cnt
                cnt +=1
        if i == len(data)-1:
            for j in range(len(data[i])):
                if data[i][R-2-j] == 0:
                    data[i][R-2-j] = cnt
                    cnt += 1
            if j == len(data[i])-1:
                # print(j)
                for i in range(len(data)):
                    if data[C-2-i][0] == 0:
                        data[C-2-i][0] = cnt
                        cnt +=1
print(data)