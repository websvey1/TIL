import sys
sys.stdin = open("미로탈출(중간).txt")

N = int(input())
arr = [[1] * (N+2) for _ in range(N+2)]
for i in range(1, N+1):
    arr[i] = [1] + list(map(int, input())) + [1]
Darr = list(map(int, input().split()))

Dno = 0
dr = [0,1,0,-1,0]
dc = [0,0,-1,0,1]
r,c = 1,1
cnt = 0
while True:
    r = r+dr[Darr[Dno]]
    c = c+dc[Darr[Dno]]
    if arr[r][c] ==0:
        arr[r][c] = 9
        cnt +=1
    elif arr[r][c]==1:
        r = r-dr[Darr[Dno]]
        c = c - dc[Darr[Dno]]
        Dno = (Dno+1) %4

    else: break
print(cnt)
for i in range(len(arr)):
    print(*arr[i])