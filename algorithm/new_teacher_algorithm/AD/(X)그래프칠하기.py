import sys
sys.stdin = open('그래프칠하기.txt')

def check(n,c):
    for i in range(n): #연결된 노드 탐색
        if arr[n][i] and rec[i]==color:return 0 # 연결된 노드와 같은색이면 실패
    return 1
def dfs(n):
    global color,flag
    if n ==N:
        flag = 1
        return
    for i in range(1,M+1): # 색칠하기
        # if arr[n][i] == 1:
        if check(n,i):
            # color +=1
            rec[n] = i
            dfs(n+1)
            if flag:return


N,M = map(int, input().split())
rec = [0] * N
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
color = 0
flag = 0
dfs(0)
# print(rec)
# print(flag)
if flag:
    for i in range(N):
        print(rec[i], end=" ")
else:
    print(-1)