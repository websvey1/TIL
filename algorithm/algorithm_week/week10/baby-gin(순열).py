def babyGin():
    global flag
    check = 0

    if arr[0] == arr[1] and arr[1] == arr[2]: check += 1
    if arr[3] == arr[4] and arr[4] == arr[5]: check += 1

    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]: check += 1
    if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]: check += 1

    if check == 2:
        flag = 1
        return


def perm(n, k):
    if k == n:
        babyGin()
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]
import sys
sys.stdin = open("baby-gin(순열).txt")

N = int(input())
for tc in range(1, N+1):
    flag =0
    arr = list(map(int, input()))
    perm(6,0)
    if flag == 1:
        print("is baby-gin")
    else:
        print("No baby-gin")