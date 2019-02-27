import sys
sys.stdin = open("색종이2.txt")
N = int(input())
empty = [[0 for _ in range(110)] for _ in range(110)]
# print(empty)
cnt = 0
for tc in range(N):
    R, C = map(int, input().split())
    for i in range(R, R+10):
        for j in range(C, C+10):
            empty[i][j] = 1

# for i in range(30):
#     for j in range(30):
#         print(empty[i][j], end = "")
#     print()

for i in range(1, 102):
    for j in range(1, 102):
        if empty[i][j] == 1:
            if empty[i-1][j] == 0: cnt +=1 #상
            if empty[i+1][j] == 0: cnt += 1  # 상
            if empty[i][j-1] == 0: cnt += 1  # 상
            if empty[i][j+1] == 0: cnt += 1  # 상
print(cnt)



