import sys
sys.stdin = open("과수우너.txt")

N = int(input())
data = [list(map(int, input())) for i in range(N)]
print(data)