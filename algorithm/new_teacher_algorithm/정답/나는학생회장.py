import sys
sys.stdin = open("in.txt")

N = int(input())
arr=[[0]*5 for _ in range(4)] # 행을 후보자로 열을 1,2,3점수대로 4열은 합계
for i in range(N):
    score = list(map(int, input().split()))
    for j in range(1, 4): # 후보자 3명
        arr[j][score[j-1]]+=1 # 후보자별 점수별 카운트

for i in range(1, 4): #후보자별 합계
    for j in range(1, 4):
        arr[i][4]+=arr[i][j]*j

maxi = 1
flag=0
for i in range(2, 4):
    if arr[maxi][4]<arr[i][4]: # 더 큰 합계를 비교
        maxi= i
        flag=0
    elif arr[maxi][4] == arr[i][4]: # 동일합계이면 3점대부터 비교
        for j in range(3, 0, -1): # 3 점대부터 비교
            if arr[maxi][j] == arr[i][j] : continue
            if arr[maxi][j] < arr[i][j]: maxi=i
            flag=0
            break
        if j==1: flag=1 # 1점대까지 갔다면 후보자 없음을 체크

if flag==0: print(maxi, arr[maxi][4])
else: print(0, arr[maxi][4])






