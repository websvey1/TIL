import sys
sys.stdin = open("소수.txt")

a,b = map(int, input().split())
# print(a)
for i in range(a,b+1):
    if i % 2 == 0 or i %3 == 0 or i % 5 == 0: