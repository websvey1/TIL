import sys
sys.stdin = open("./tc/special_sort.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)
    result = []
    while data != []:
        result.append(max(data))
        data.pop(data.index(max(data)))
        result.append(min(data))
        data.pop(data.index(min(data)))
    print("#%d" %(tc), end=" ")
    print(*result[:10])