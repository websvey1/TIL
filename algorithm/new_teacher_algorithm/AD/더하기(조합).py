# import sys
# sys.stdin = open('더하기.txt')
def dfs(n, cnt):
    global F
    if F : return  # 가지치기
    if n == N:
        if sum(box) == a:
            F = 1
            print(box)
            return
        return
    box[cnt]=data[n]
    dfs(n+1, cnt+1)
    if F: return  # 가지치기
    box[cnt] = 0
    dfs(n+1, cnt)

T = int(input())
for tc in range(1,T+1):
    N, a = list(map(int, input().split()))
    data = list(map(int, input().split()))
    box = [0 for _ in range(N)]
    cnt = 0
    F = 0

    dfs(0, cnt)
    if F ==1:
        print('YES')
    else:
        print('NO')

#########################################################
################################ 기철이형#################3
######################################################### 
# def DFS(no, ssum):
#     global flag, N, K
#     if flag or ssum > K: return
#
#     if no >= N:
#         if ssum == K:
#             flag = 1
#         return
#
#     DFS(no+1, ssum + di_arr[no])
#     DFS(no+1, ssum)
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())   # 갯수 N, 합 K
#     di_arr = list(map(int, input().split()))
#
#     flag = 0
#     DFS(0,0)
#     if flag :
#         print('YES')
#     else:
#         print('NO')