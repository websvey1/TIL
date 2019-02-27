import sys
sys.stdin = open("색종이1.txt")
N = int(input())
empty = [[0 for _ in range(100)] for _ in range(100)]
# print(empty)
cnt = 0
for tc in range(N):
    R, C = map(int, input().split())
    for i in range(R, R+10):
        for j in range(C, C+10):
            empty[i][j] = 1

for i in range(30):
    for j in range(30):
        print(empty[i][j], end = "")
    print()
for i in range(100):
    for j in range(100):
        if empty[i][j] == 1:
            cnt += 1
print(cnt)



