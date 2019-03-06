def find(t):
    for i in range(N):
        for j in range(N):
            if t in data[i]:
                data[i][data[i].index(t)] =0
                return data

def isbingo(d):
    global result
    for i in range(N):
        cnt = 0
        for j in range(N):
            if d[i][j] == 0:
                cnt +=1
        if cnt == N:
            result +=1
            return result
import sys
sys.stdin = open("빙고.txt")

N = 5
data = [list(map(int, input().split())) for i in range(N)]
answer = [list(map(int, input().split())) for i in range(N)]
result = 0
# for i in range(N):
    # print(*data[i])

# for i in range(N):
    # print(*answer[i])

for i in range(N):
    for j in range(N):
        find(answer[i][j])
        isbingo(data)

print(result)

