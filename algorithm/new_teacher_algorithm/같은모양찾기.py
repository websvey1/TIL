import sys
sys.stdin = open("같은모양찾기.txt")

def find(i,j):
    for k in range(t):
        for l in range(t):
            if data[i+k][j+l] != answer[k][l]:
                return 0
    return 1

T = int(input()) # 10
# empty = [[0 for _ in range(100)] for _ in range(100)]
data = [input() for _ in range(T)]
t = int(input()) # 3
answer = [input() for _ in range(t)]
cnt = 0

for i in range(T-t+1):
    for j in range(T-t+1):
        cnt += find(i,j)

print(cnt)




