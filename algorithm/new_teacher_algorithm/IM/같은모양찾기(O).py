import sys
sys.stdin = open("같은모양찾기.txt")


T = int(input())
data = [list(map(int, input())) for _ in range(T)]
t = int(input())
target = [list(map(int, input())) for _ in range(t)]
find = 0

for i in range(T-t+1):
    for j in range(T-t+1):
        cnt = 0
        for k in range(t):
            for L in range(t):
                if data[i+k][j+L] == target[k][L]:
                    cnt +=1
        if cnt == 9:
            find +=1
print(find)