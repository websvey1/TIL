import sys
sys.stdin = open("표준입출력.txt")

# n = int(input())
# a,b = map(int, input().split())
# for i in range(a):
#     print(input())


####강사님
T = int(input())
r,c = list(map(int, input().split()))
arr = [list(map(int, input())) for _ in range(r)]

print(T)
for i in range(r):
    for j in range(c):
        print(arr[i][j], end="")
    print()