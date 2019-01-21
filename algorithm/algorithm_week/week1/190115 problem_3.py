import sys
sys.stdin = open("input_3.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    first = sum(data[0:M])
    num_max = first
    num_min = first
#    hap = 0
    # print(N, data)
    for i in range(1, len(data)-M+1):
        a = data[i:i+M]
        hap=0
        for j in a:
           hap += j
        if num_max < hap:
            num_max = hap
        if num_min > hap:
            num_min = hap
    result = num_max - num_min
    print(f'#{test_case}', result)