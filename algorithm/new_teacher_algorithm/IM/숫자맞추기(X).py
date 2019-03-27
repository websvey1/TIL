import sys
sys.stdin = open("숫자맞추기.txt")

N = int(input())
# for t in range(T):
data = [input().split() for _ in range(N)]
# data = int(data)
data_copy = [[0 for _ in range(len(data[0]))] for _ in range(N)]

for i in range(len(data_copy)):
    for j in range(len(data_copy[i])):
        data_copy[i][j] = int(data[i][j])
print(data_copy)
for i in range(len(data_copy)):
    for j in range(len(data_copy[i])):
        data_copy[j][i] # 포기