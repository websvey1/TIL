import sys
sys.stdin = open('최소비용.txt')

# def dfs1(n,hap): # 현재 행에서 모든 열을 사용하는 경우의 수
#     global answer_b
#     if hap > answer_b:return
#     if n == N:
#         for i in range(N): print(chk[i], end=' ')
#         print(hap)
#         if hap < answer_b:
#             answer_b = hap
#         return
#
#     for i in range(N): # 열
#         chk[n]=data[n][i]
#         # if answer_b < hap:return # 여기가 가지치기가 아니다!!!!!
#         dfs1(n + 1, hap+data[n][i])

def dfs2(n,hap):
    global answer_b
    if hap > answer_b:return # 가지치기 합이 answer_b를 초과시 리턴
    if n == N:
        # for i in range(N): print(chk[i], end=' ')
        # print(hap)
        if hap < answer_b:
            answer_b = hap
        return

    for i in range(N): # 열
        if chk2[i]:continue
        chk2[i]=1
        chk[n]=data[n][i]
        dfs2(n + 1, hap+data[n][i])
        chk2[i]=0
##############################################3
####################내가한거####################
##############################################3
# def dfs(n,hap):
#     global answer_b
#     if hap > answer_b:return
#     if n == N:
#         if hap < answer_b:
#             answer_b = hap
#         return
#
#     for i in range(N):
#         for j in range(N):
#             if chk[i] !=0:continue
#             chk[i] = 1
#             hap += data[i][j]
#             if hap <answer_b:
#                 dfs2(n+1,hap)
#                 chk[i] = 0

N = int(input())
data = [list(map(int, input().split()))for _ in range(N)]
chk = [0 for _ in range(N)] # 고른값을 기록
chk2 = [0 for _ in range(N)] # 열 체크 배열
# print(chk)
# print(N,data)
answer_a = 0
answer_b = 9999999999999999999999999999
hap = 0
for i in range(N):
    answer_a += min(data[i])
print(answer_a)
# dfs1(0,hap) # 0행부터 시작 , 열의 중복을 허용한 중복순열
dfs2(0,hap)
print(answer_b)