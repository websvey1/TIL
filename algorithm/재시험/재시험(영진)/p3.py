import sys
import time
s_time = time.time()

sys.stdin = open('../p3.txt')

def stick(n, sums):
    global flag

    if sums > L:
        return

    if n == N:
        if sums == L:
            flag = 1
        return

    stick(n+1, sums + arr[n])
    stick(n+1, sums)


for tc in range(int(input())):
    N, L = map(int, input().split())
    arr = list(map(int, input().split()))
    chk = [0] * N
    flag = 0
    stick(0, 0)

    print('#{} '.format(tc+1), end='')

    if flag:
        print(1)
    else:
        print(0)