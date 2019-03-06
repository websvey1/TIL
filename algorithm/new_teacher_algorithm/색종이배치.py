import sys
sys.stdin = open("색종이배치.txt")
# empty = [[0 for _ in range(100)] for _ in range(100)]
# comp_empty = [[0 for _ in range(100)] for _ in range(100)]
# comp2_empty = [[0 for _ in range(100)] for _ in range(100)]
# # print(empty)
# cnt = 0
# comp_cnt = 0
# comp2_cnt=0
# for t in range(2):
#     S,E,W,H = map(int,input().split())
#     for i in range(S, S+W):
#         for j in range(E, E+H):
#             empty[i][j] += 1
#             cnt +=1
#
# for z in range(30):
#     for x in range(30):
#         print(empty[z][x], end="")
#     print()
# print(cnt)


sr, sc, w, h = map(int, input().split())
arr = [[0] * 100 for i in range(100)]

for i in range(sr - 1, sr + h + 1):
    for j in range(sc - 1, sc + w + 1):
        if i == sr - 1 or i == sr + h or j == sc - 1 or j == sc + w:
            arr[i][j] = 2
        else:
            arr[i][j] = 1

sr, sc, w, h = map(int, input().split())
cnt1 = 0
cnt2 = 0
for i in range(sr, sr + h):
    for j in range(sc, sc + w):
        if arr[i][j] == 1:
            cnt1 += 1
        elif arr[i][j] == 2:
            cnt2 += 1

if cnt1 == 0 and cnt2 == 1:
    sol = 1
elif cnt1 == 0 and cnt2 > 1:
    sol = 2
elif cnt1 > 0:
    sol = 3
else:
    sol = 4

print(sol)






































# for t in range(2):
#     for i in range(S, S+W):
#         for j in range(S, S+H):
#             comp_empty[i][j] +=1
#             comp_cnt +=1
#     for i in range(E, E+W):
#         for j in range(E, E+H):
#             comp2_empty[i][j] +=1
#             comp2_cnt +=1
#
# for k in range(100):
#     # for l in range(100):
#     if 2 in empty[k]:
#         print("3")
#         break
# if comp_cnt != comp2_cnt:
#     print("2")
# else:
#     print("1,4")
# print(comp_cnt)
