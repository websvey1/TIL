def hap():
    global N, result
    hap = 0
    hap += data[0][arr[0]]
    for i in range(N-2):
        hap += data[arr[i]][arr[i+1]]
    hap += data[arr[-1]][0]
    result = min(hap,result)


def perm(n, k):
    if k == n:
        hap()
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            # print(k,n, end=" ")
            perm(n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]

import sys
sys.stdin = open("전기카트.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split()))for _ in range(N)]
    arr = list(range(1,N))
    # print(arr)
    result = 99999999
    perm(N-1, 0)

    print('#%d %d' %(tc,result))
