import sys
sys.stdin = open('길찾기.txt')
def bfs(x,y):
    q = []
    visit[n] = 1
    q.append(n)
    while q:
        a = q.pop(0)
        for i in range(100):
            if arr[a][i] == 99:
                flag = 1
                return
            elif arr[a][i] == 1 and visit[i]==0:
                visit[i] = 1
                q.append(i)
    return

for _ in range(1):
    tc, n = map(int, input().split())
    arr = [[0 for _ in range(100)]for _ in range(100)]
    data = list(map(int, input().split()))
    visit = [0] * 100
    flag = 0
    for i in range(0,n*2,2):
        arr[data[i]][data[i+1]] = 1

    bfs(0,0)
    print('#%d %d' %(tc, flag))