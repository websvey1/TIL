# def hap(N):
#     global cnt
#     if N==0:
#         return cnt
#     else:
#         cnt += N
#         hap(N-1)
def hap(i):
    global cnt
    if i >N:
        return cnt
    cnt +=i
    # print(cnt)
    hap(i+1)
N = int(input())
cnt = 0
hap(1)
print(cnt)