import sys
sys.stdin = open('길찾기.txt')

def dfs(n):
    global flag
    if n == 99:
        flag = 1
        return
    visit[n] = 1
    for A in range(100):
        if arr[n][A] == 1 and visit[A]==0:
            dfs(A)
for _ in range(10):
    tc, n = map(int, input().split())
    arr = [[0 for _ in range(100)]for _ in range(100)]
    data = list(map(int, input().split()))
    visit = [0] * 100
    flag = 0
    for i in range(0,n*2,2):
        arr[data[i]][data[i+1]] = 1
    # for Z in range(100):
    #     print(*arr[Z])
    # print(data)
    dfs(0)
    print('#%d %d' %(tc, flag))