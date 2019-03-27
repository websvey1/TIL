import sys
sys.stdin = open("도약.txt")
###########################################################
########################## 두개 쓰기 ########################
###########################################################
# def lowerSearch(s,e,f):
#     # f 이상 중에서 가장 작은 값의 위치를 리턴
#     sol = -1
#     while s<=e:
#         m = (s+e)//2
#         if data[m] >= f: # f 이상이면 왼쪽영역 재탐색(더 작은 값 찾기 위해)
#             sol = m
#             e = m-1
#         else:
#             s= m+1 #우측탐색)
#     return sol
#
# def upperSearch(s,e,f):
#     # f 이하중에서 가장 큰 값의 위치를 리턴
#     sol = -1
#     while s<=e:
#         m = (s+e)//2
#         if data[m] <= f: # 데이타 이하면 오른쪽 재탐색(더 큰걸 찾기위해)
#             sol = m
#             s = m+1
#         else:
#             e= m-1
#     return sol
# N = int(input())
# data = sorted([(int(input())) for i in range(N)])
# cnt = 0
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         S = data[j]+(data[j]-data[i])
#         E = data[j] + (data[j] - data[i])*2
#         lo = lowerSearch(j+1, N-1, S)
#         if lo==-1 or data[lo]>E: continue
#         up = upperSearch(j+1, N-1, E)
#         cnt += (up-lo+1)
# print(cnt)
###########################################################
########################## 하나 쓰기########################
###########################################################

def upperSearch(s,e,f):
    # f 이하중에서 가장 큰 값의 위치를 리턴
    sol = -1
    while s<=e:
        m = (s+e)//2
        if data[m] < f: # 데이타 이하면 오른쪽 재탐색(더 큰걸 찾기위해)
            s = m + 1
            sol = m
        else:
            e= m-1
    return sol
N = int(input())
data = sorted([(int(input())) for i in range(N)])
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        S = data[j]+(data[j]-data[i])
        E = data[j] + (data[j] - data[i])*2
        cnt += upperSearch(j, N- 1, E+1) - upperSearch(j, N-1, S)
print(cnt)
