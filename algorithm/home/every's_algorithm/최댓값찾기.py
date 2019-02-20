# a = [14, 2, 15, 345, 1235, 135, 183]
# cnt = 0
# for i in range(1, len(a)):
#     if a[i] > a[cnt]:
#         cnt = i
# print(cnt)


## 1부터 n까지 합 재귀

# def hap(n):
#     if n ==1:
#         return 1
#     else:
#         return n+ hap(n-1)
#
# print(hap(100))



# 숫자 n개중에서 최댓갑 찾기
def max_n(L, N):
    if N == 1:
        return L[0]
    comp = max_n(L, N-1)
    if comp > L[N-1]:
        return comp
    else:
        return L[N-1]

print(max_n([1,3,5,7,9], 5))