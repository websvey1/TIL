import sys
sys.stdin = open("problem_4.txt", "r")

T = int(input())
for i in range(1, T+1):
    N = int(input())
    n = list(map(int, input().split()))
    asc_list = des_list = n[:]
    for j in range(len(n)-1):
        min_idx = j
        for k in range(j+1, len(n)):
            if n[min_idx] > n[k]:
                min_idx = k
        asc_list[j], asc_list[min_idx] = asc_list[min_idx], asc_list[j]              # 여기서 indent가 두번 들어갔었음.

    for j in range(len(n)-1):
        max_idx = j
        for k in range(j+1, len(n)):
            if n[max_idx] < n[k]:
                max_idx = k
        des_list[j], des_list[max_idx] = des_list[max_idx], des_list[j]
    print(des_list)
