import sys
sys.stdin = open("in.txt")

N, K = map(int, input().split())
arr=[]
for i in range(N):
    arr.append(list(map(int, input().split())))

def check(si, sj): # 현재 위치에서 도넛모양의 합계구하는 함수
    dsum=0
    for i in range(si, si+K):
        for j in range(sj, sj+K):
            if j==sj or j==sj+K-1 : # 시작열, 도넛끝열 더하기
                dsum+=arr[i][j]
            if (i==si or i==si+K-1) and sj<j<sj+K-1:#중간열 더하기
                dsum+=arr[i][j]
    return dsum

sol=0
for i in range(N-K+1): # 맵의 시작행 제어
    for j in range(N-K+1): #맵의 사작열 제어
        dsum= check(i, j)
        if dsum> sol: sol=dsum
print(sol)