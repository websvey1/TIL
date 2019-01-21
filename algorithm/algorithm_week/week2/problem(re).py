
import sys
sys.stdin = open("problem.txt")

T = 10
for test_case in range(1, T + 1):
    N = input()
    a = [[0 for _ in range(100)] for _ in range(100)]
    max_sum = 0
    max_list = []
    for i in range(100):
        a[i] = list(map(int, input().split()))
    for i in range(len(a)):
        garo = 0
        for j in range(len(a[i])):
            garo += a[i][j]
        if max_sum < garo:
            max_sum = garo
        max_list.append(garo)
    dagag = 0
    dagag2 = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i == j:
                dagag += a[i][j]
            if i+j == 99:
                dagag2 += a[i][j]
    # print(dagag)
    max_list.append(dagag2)
    max_list.append(dagag)

    for j in range(len(a[0])):
        sero = 0
        for i in range(len(a)):
            sero += a[i][j]
        if max_sum < sero:
            max_list.append(sero)
    # print()
    print(f'#{test_case} {max(max_list)}')
