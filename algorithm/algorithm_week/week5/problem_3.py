import sys
sys.stdin = open("problem_3.txt")

def compare(a,b):
    if (a,b) == (1,3) or (a,b) == (3,1) :
        return 1
    elif a < b:
        return b
    elif a > b:
        return a
    # elif a == b:
    if
    # 이부분을 재귀로 좀더 완성하면 될것같은데.


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    dict_data = {}
    win_list = []
    for i in range(1, N+1):
        dict_data[i] = data[i-1]
    # print(N, data)
    # print(dict_data)
    for k,v in dict_data.items():
        win_list.append([k,v])
    # print(win_list)
    for j in range(0, len(win_list),2):
        # compare(win_list[j][1], win_list[j+1][1])
        if win_list[j][1] > win_list[j+1][1]:
            win_list.pop(j+1)
        else:
            win_list.pop(j)