import sys, time
from time import strftime
sys.stdin = open("최적경로.txt")

start_time = time.time()

def perm(n, k, length):
    global result
    if length >= result:      #length는 초기 0
        return
    if n == k:                  #n과 k가 같을때까지 쌓이다가, 같으면서 return
        length = 0
        stack = []
        stack.append(work)
        for i in N_list:
            stack.append(i)
        stack.append(home)
        # print(stack)
        for i in range(len(stack) - 1):
            x = stack[i][0]
            y = stack[i][1]
            nx = stack[i + 1][0]
            ny = stack[i + 1][1]
            length += abs(nx - x) + abs(ny - y)
        result = min(result, length)
    else:
        for i in range(k, n):
            N_list[i], N_list[k] = N_list[k], N_list[i]
            perm(n, k + 1,0)
            N_list[i], N_list[k] = N_list[k], N_list[i]


T = 10
for tc in range(1, T + 1):
    N = int(input())
    raw = list(map(int, input().split()))  # 전체데이터
    work = [raw[0], raw[1]]  # 회사
    home = [raw[2], raw[3]]  # 집
    N_list = []                        # 데이터
    for i in range(4, len(raw), 2):
        N_list.append([raw[i], raw[i + 1]])    # 데이터를 이중리스트로 넣음
    print(N_list)
    result = float('inf')        # 이거 뭐냐 = 가장 큰 수
    perm(N, 0, 0)

    print('#{} {}'.format(tc, result))

print(time.time() - start_time, 'seconds')