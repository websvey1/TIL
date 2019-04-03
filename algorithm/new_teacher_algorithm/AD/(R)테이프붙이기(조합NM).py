import sys
sys.stdin = open('테이프붙이기.txt')

def dfs(no, cnt, hap):
    global sol
    if cnt +(N-no) <N/2:return # 가지치기. 앞으로 더할 개수 < N의절반일때 시행x
    if cnt == N // 2:  # N/2개를 고른 경우만 길이의 차 비교
        for i in range(N):
            print(rec[i], end=" ")
        print('cnt=',cnt,'hap=',hap)
        temp = abs(hap - (tot - hap))  # 이등분한 테이프의 차이
        if temp < sol: sol = temp
        return
    if no >=N:
        # for i in range(N):
        #     print(rec[i], end=" ")
        # print('cnt=',cnt,'hap=',hap)
        return
    # 현재 no번 테이프를 붙이거나 붙이지 않는 경우의 시도
    rec[cnt] = data[no]
    dfs(no+1, cnt+1, hap+data[no])
    rec[cnt]=0
    dfs(no+1, cnt, hap)



N = int(input())
data = list(map(int, input().split()))
rec = [0] * N
sol = 500 * 20
tot = sum(data)
dfs(0,0,0) # 0번째 테이프부터 시작, 고른개수0개, 테이프길이합0