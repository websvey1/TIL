N = int(input())
arr=[[9]*(N+2) for _ in range(N+2)]
for i in range(1, N+1):
    for j in range(1, N+1):
        arr[i][j]=0

K = int(input())
for i in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 8

L = int(input())
time=[0]*10001
for i in range(L):
    X, C =input().split()
    X= int(X)
    if C == 'L': time[X]=1
    else: time[X]=2

dr = [0, -1, 1, 0 ,0]
dc = [0, 0,0, -1, 1]
turn = [[0,0,0],[0,3, 4], [0,4, 3], [0,2, 1], [0,1,2]]

tcnt=0
r, c=1,1
er, ec = 1,1
ndir = 4
arr[r][c]= ndir
# for i in range(N+2):
#     for j in range(N+2):
#         print(arr[i][j], end=' ')
#     print()

while True:
    r+=dr[ndir]
    c+=dc[ndir]
    tcnt+=1
    if time[tcnt] : ndir = turn[ndir][time[tcnt]]

    if arr[r][c]==8:
        arr[r][c]=ndir
    elif arr[r][c] == 9 or 0<arr[r][c]<5:
        break
    elif arr[r][c]==0:
        arr[r][c]=ndir
        enddir=arr[er][ec]
        arr[er][ec] = 0
        er+= dr[enddir]
        ec+=dc[enddir]



print(tcnt)
