import sys
sys.stdin = open("problem_4.txt", "r")

T = int(input())
# print(T)
for tc in range(1, T+1):
    data = list(input())
    i = 0
    while i < len(data)-1:
        if data[i] == data[i+1]:
            del data[i+1],
            del data[i]
            i = 0
        else:
            i += 1
    print(f'#{tc} {len(data)}')
    # print(data)3
