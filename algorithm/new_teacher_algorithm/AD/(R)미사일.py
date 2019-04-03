import sys
sys.stdin = open('미사일.txt')
def clear(n):
    for i in range(N): # i 는 비교대상
        temp = abs(ship[n][0]-ship[i][0])+abs(ship[n][1]-ship[i][1])
        if temp <=R:
            ship[i][2] -= P
def update(n):
    for i in range(N): # i 는 비교대상
        temp = abs(ship[n][0]-ship[i][0])+abs(ship[n][1]-ship[i][1])
        if temp <=R:
            ship[i][2] += P
def dfs(n):
    global sol
    if n==M:
        cnt = 0
        for i in range(N):
            if ship[i][2]>0: cnt +=1
        if cnt<sol: sol=cnt
        return

    else:
        for i in range(len(ship)):
            if ship[i][2] <=0: continue # 침몰하지 않은 군함에만 시도
            clear(i)
            dfs(n+1) # 다음 미사일로
            update(i)

N = int(input())
ship = [list(map(int, input().split()))for _ in range(N)]
M,P,R = map(int, input().split())
# print(ship)
sol = float('inf')
a = [0]*N
dfs(0)
print(sol)