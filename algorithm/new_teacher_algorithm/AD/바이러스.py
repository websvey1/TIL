import sys
sys.stdin = open('바이러스.txt')

#BFS,

# 플루트 필?

def FF(n):
    global sol
    chk[n] = 1 # 이위치에 있으면 1번컴퓨터를 체크하는것.
    for i in range(1,C+1):
        if arr[n][i] == 1 and chk[i] ==0: # n현재 내 위치, i는 다음거 위치.
            sol +=1
            arr[n][i] = 0
            FF(i)
C = int(input())
N = int(input())
data = [list(map(int, input().split()))for _ in range(N)]
# print(data)
chk = [0] * (C+1)
arr = [[0 for _ in range(C+1)]for _ in range(C+1)]
for i in range(N):
    arr[data[i][0]][data[i][1]] = 1
    arr[data[i][1]][data[i][0]] = 1
# for i in range(C+1):
#     print(*arr[i])
sol = 0
FF(1) #1번 컴퓨터부터 시작
print(sol)