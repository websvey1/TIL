import sys
sys.stdin = open("./tc/color.txt", "r")

T = int(input())
def chk():
    tmp = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] ==3:
                tmp +=1
    return tmp

for tc in range(1,T+1):
    arr = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    N = int(input())
    for n in range(N):
        x1,y1,x2,y2,c = map(int, input().split())
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if arr[i][j] == 0:
                    arr[i][j] = c
                elif arr[i][j] != c:
                    arr[i][j] += c
    cnt = chk()
    # print(arr)
    # print(cnt)
    print("#%d %d" %(tc,cnt))
# print(arr)
