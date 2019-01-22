import sys
sys.stdin = open("problem_3.txt", "r")

# def compare(num):
#     for i in range(10):
#         start = 0
#         end = P
#         center = (start + end) // 2
#         cnt_a += 1
#         if center > num:
#             start = num
#             end = P
#         elif P < num:
#             start = P
#             end = num
#         else:
#             break
#         return
T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    cnt_a= cnt_b = 0
    start = 1
    end = P
    for i in range(10):
        center = (start + end) // 2
        cnt_a += 1
        if center > A:
            end = center
        elif center < A:
            start = center
        else:
            break

    start = 1
    end = P
    for i in range(10):
        center = (start + end) // 2
        cnt_b += 1
        if center > B:
            end = center
        elif center < B:
            start = center
        else:
            break
    if cnt_a < cnt_b:
        print(f"#{tc}", "A")
    elif cnt_a > cnt_b:
        print(f"#{tc}", "B")
    else:
        print(f"#{tc}", "0")
###############################################################     원래짯던코드
#     for i in range(10):
#         if P != A:
#             P = P // 2
#             cnt_a += 1
#         else:
#             break
#     for j in range(10):
#         if P != B:
#             P = (B + P) // 2
#             cnt_b += 1
#         else:
#             break
#     if cnt_a < cnt_b:
#         print(f"#{tc}", "A")
#     elif cnt_a > cnt_b:
#         print(f"#{tc}", "B")
#     else:
#         print(f"#{tc}", "0")
# ##############################