import sys
sys.stdin = open('주사위2.txt')
# def jusawi(n):   # n번째 주사위, 시작은 1
#     data = [0 for _ in range(7)]
#     if n>a:       #a는 주사위 던짓 횟수
#         print(data)
#         return
#     else:
#         for i in range(1,7):
#             data[n] = i
#             jusawi(n+1)
# a,b = map(int,input().split())
# jusawi(1)

#########################################
###############강사님####################3
#########################################

# def dfs(no,hap):
#     if no>N:
#         if hap == M:
#             for i in range(1,N+1):print(rec[i], end=' ')
#             print()
#         return
#     for i in range(1,7):
#         if chk[i]:continue
#         rec[no] = i
#         dfs(no+1,hap+i)
#         chk[i]=0

def dfs(n,hap):
    if n >N:
        if hap==M:
            for i in range(len(rec)):
                if rec[i]:
                    print(rec[i], end=" ")
            print()

        return
    for i in range(1,7):
        rec[n] = i

        if chk[i]: continue
        chk[i] = 1
        dfs(n+1,hap+i)
        chk[i] = 0

N,M = map(int, input().split()) #N번 던져서 합이 M
rec = [0] * 8  # 주사위 데이터 입력
chk = [0] * 7 # 주사위 체크
hap = 0 #합계를 넘길 것
dfs(1,hap)











