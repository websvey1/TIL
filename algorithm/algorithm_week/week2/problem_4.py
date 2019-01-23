import sys
sys.stdin = open("problem_4.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = list(map(int, input().split()))
    asc_list = n[:]
    des_list = n[:]
    for j in range(len(n)-1):
        min_idx = j
        for k in range(j+1, len(n)):
            if asc_list[min_idx] > asc_list[k]:
                min_idx = k
        asc_list[j], asc_list[min_idx] = asc_list[min_idx], asc_list[j]              # 여기서 indent가 두번 들어갔었음.

    for j in range(len(n)-1):
        max_idx = j
        for k in range(j+1, len(n)):
            if des_list[max_idx] < des_list[k]:
                max_idx = k
        des_list[j], des_list[max_idx] = des_list[max_idx], des_list[j]
    # print(asc_list)
    asc_list_cut = asc_list[0:len(asc_list)//2]
    des_list_cut = des_list[0:len(des_list)//2]
    result = []
    for i in range(5):
        result.append(des_list_cut[i])
        result.append(asc_list_cut[i])
    print(f'#{tc}', *result)
    # print(*result)