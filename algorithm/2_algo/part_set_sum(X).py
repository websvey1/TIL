import sys
sys.stdin = open("./tc/part_set_sum.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, S = map(int, input().split())
    data = list(range(0,13))
    print(data)