import sys
sys.stdin = open("problem_3.txt", "r")
T = int(input())
for tc in range(1, T+1):
    comp = input()
    total = input()
    len_comp = len(comp)
    len_total = len(total)
    empty_list = [0] * len_comp
    result = 0
    # print(empty_list)
    for i in range(len_comp):
        for j in range(len_total):
            if total[j] == comp[i]:
                empty_list[i] += 1
    result = max(empty_list)
    print(f'#{tc} {result}')