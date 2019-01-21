import sys
sys.stdin = open("input_workshop.txt")
n = int(input())
a = list(map(int, input().split()))
max_num = a[0]
min_num = a[0]
cnt = 0
for i in range(0, len(a)):
    while cnt < n:
        if a[i] > max_num:
            max_num = a[i]
        if a[i] < min_num:
            min_num = a[i]
        # print(max_num, min_num)
        a[a.index(max_num)] -= 1
        a[a.index(min_num)] += 1
        cnt += 1
print(cnt, min_num, max_num)


for i in range(10):
    howmany = int(input())
    boxes = list(map(int, input()))
    n = 0
    while n < howmany:
        mickey = max(boxes)
        mini = min(boxes)
        if mickey - mini <=1:
            print(f"#{i} {mickey- mini}")
            break
        boxes[boxes.index(mickey)] -= 1
        boxes[boxes.index(mini)] += 1
        n=n+1
        print(n)
    else:
        mickey = max(boxes)
        mini = min(boxes)
        print(f"#{i} {mickey-mini}")

import sys
sys.stdin = open("Flatten_input.txt")





#
# for n in range(1, 11):
#     N = int(input())
#     boxes = list(map(int, input().split()))
#     cnt = 0
#     for T in range(N):
#         for i in range(len(boxes) - 1, 0, -1):
#             for j in range(i):
#                 if boxes[j] < boxes[j + 1]:
#                     boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
#         boxes[0] += -1
#         boxes[-1] += 1
#     for i in range(len(boxes) - 1, 0, -1):
#         for j in range(i):
#             if boxes[j] < boxes[j + 1]:
#                 boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
#     max_num = boxes[0]
#     min_num = boxes[-1]
#     result = max_num - min_num
#     print(f'#{n} {result}')