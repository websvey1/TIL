import sys
sys.stdin = open("../덧셈.txt")

num, X = map(int, input().split())
arr = str(num)
N = len(arr)
#2개 정수로 분리
# for i in range(N-1):
#     A = int(arr[:i+1])
#     B = int(arr[i+1:])
#     print(A,B)

#3개정수로 분리
for i in range(N-2):
    A = int(arr[:i+1])
    for j in range(i+1,N-1):
        B=int(arr[i+1:j+1])
        C=int(arr[j+1:])
        print(A,B,C)
