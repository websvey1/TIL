def find(s,e,fdata):

    global cnt
    cnt = 0
    while s <=e:
        m = (s + e) // 2
        if fdata == data[m]:
            return m + 1
        elif fdata > data[m]:
            s = m+1
        elif fdata< data[m]:
            e = m-1
    return 0
import sys
sys.stdin = open('숫자찾기.txt')

N = int(input())
data = list(map(int, input().split()))
fN = int(input())
fdata = list(map(int, input().split()))
cnt = 0

for i in range(fN):
    a =find(0, N-1, fdata[i])
    print(a)

#######################################
################개야매 #################
#######################################
# for i in range(fN):
#     if fdata[i] in data:
#         print(data.index(fdata[i])+1)
#     else:
#         print(0)

########################################
#################정석 ###################
########################################
# def find(s,e,fdata):
#     global cnt
#     cnt = 0
#     while s<=e:
#         mid = (s + e ) // 2
#         cnt += 1
#         if fdata == data[mid]: # mid번 째 값이 fdataㅇ면 mid + 1 리턴
#             return mid + 1
#         elif fdata > data[mid]:
#             s = mid + 1
#         elif fdata < data[mid]:
#             e = mid -1
#     return 0
#
#
# for i in range(fN):
#     a = find(0,N-1, fdata[i])
#     print(a)
