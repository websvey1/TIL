a = [9,8,7,6,5,4,3,6,2,1]
# # 일반적인 정렬
# for i in range(len(a)-1):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             a[i], a[j] = a[j] , a[i]
# print(a)

####################################################################
####################################################################
# 퀵정렬
# def Qsort(s,e):
#     if s >= e:
#         return
#     else:
#         P = e
#         T = s
#         for L in range(s,e+1): # e+1인지 e인지?
#             if a[L] < a[P]:
#                 a[L],a[T] = a[T], a[L]
#                 T +=1
#         a[P], a[T] = a[T],a[P]
#         Qsort(s,T-1)
#         Qsort(T+1,e)
#
# s = 0
# e = len(a)-1
# Qsort(s,e)
# print(a)
####################################################################
####################################################################

#머지 정렬
def Merge(s,e):
    if s >=e:return
    m = (s+e)//2   # 중간으로 나눔
    Merge(s,m)     # 중간 왼쪽 재귀
    Merge(m+1,e)   # 중간 오른쪽 재귀
    L,R,T = s,m+1,s   # L 왼쪽초기값, R 오른쪽 초기값 T = 임시버퍼 초기값
    while L<=m and R<=e:   #
        if a[L] < a[R]: # 왼쪽이 작으면 왼쪽값을 버퍼로
            temp[T] = a[L]
            L += 1
            T +=1
        else:
            temp[T] = a[R]
            R += 1
            T +=1
    while L<=m: #
        temp[T] = a[L]
        T +=1
        L +=1
    while R <=e:
        temp[T] = a[R]
        T +=1
        R +=1
    for i in range(s, e+1):
        a[i] = temp[i]
s  = 0
e = len(a)-1
temp = [0 for _ in range(e+1)]
Merge(s,e)
print(a)
print(temp)
