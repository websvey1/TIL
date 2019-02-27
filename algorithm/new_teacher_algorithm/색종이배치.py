import sys
sys.stdin = open("색종이배치.txt")
empty = [[0 for _ in range(100)] for _ in range(100)]
comp_empty = [[0 for _ in range(100)] for _ in range(100)]
comp2_empty = [[0 for _ in range(100)] for _ in range(100)]
# print(empty)
cnt = 0
comp_cnt = 0
comp2_cnt=0
for t in range(2):
    S,E,W,H = map(int,input().split())
    for i in range(S, S+W):
        for j in range(E, E+H):
            empty[i][j] += 1
            cnt +=1

for z in range(30):
    for x in range(30):
        print(empty[z][x], end="")
    print()
print(cnt)














































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
