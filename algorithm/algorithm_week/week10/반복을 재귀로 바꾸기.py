A = [1, 5, 3, 2, 9, 7]

##########3 반복문 ###################
# def SelectionSort(A):
#     n = len(A)
#     for i in range(0, n-1):
#         min = i
#
#         for j in range(i+1, n):
#             if A[j] < A[min]:
#                 min=j
#         temp = A[min]
#         A[min] = A[i]
#         A[i] = temp
#
#
#     return A
# print(SelectionSort([1,5,3,2,9,7]))


################## 재귀 ########################
# def recelectionsort(A, s, e):
#     mini = s
#     if s == e: return
#
#     for j in range(s+1, e, 1):
#         if A[j] < A[mini]:
#             mini = j
#     A[s], A[mini] = A[mini], A[s]
#     recelectionsort(A, s+1, e)
#
# print(recelectionsort(A,0,5))
# print(A)

############# 내 재귀 #####################이게 어떻게 도는지 꼭 확인하기
def SelectionSort(A,s,e):
    min = s
    if s == e:
        return

    for j in range(s+1,e,1):
        if A[min] > A[j]:
            min = j
    A[s], A[min] = A[min], A[s]
    SelectionSort(A,s+1,e)

print(SelectionSort(A,0,5))
print(A)

