import sys
import time
from time import strftime

sys.stdin = open("최적경로.txt")

def perm(n, k):
    global length
    sums = 0
    total = work + save + home
    for i in range(k+1):
        sums += abs(total[i][0] - total[i + 1][0]) + abs(total[i][1] - total[i + 1][1])
        if length != 0 and sums > length:
            return

    if n == k:
        if (sums < length) or (not length):
            length = sums

    else:
        for i in range(k, n):
            save[i], save[k] = save[k], save[i]
            perm(n, k+1)
            save[i], save[k] = save[k], save[i]



start_time = time.time()

T = 10

for n in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    work = [[arr[0], arr[1]]]
    home = [[arr[2], arr[3]]]
    save = [[arr[i], arr[i+1]] for i in range(4, 2*(N+2), 2)]
    # print(save)
    length = 0

    perm(N, 0)
    print("#{0} {1}".format(n, length))

print(time.time() - start_time, 'second')