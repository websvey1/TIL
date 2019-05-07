import sys
sys.stdin = open('0505_cattle_defence.txt')

N,M,D = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
print(data)