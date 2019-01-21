
import sys
sys.stdin = open("problem.txt")

T = 10
for test_case in range(1, T + 1):
    N = input()
    a = [[0 for _ in range(100)] for _ in range(100)]
    max_sum = 0
    max_list = []
    for i in range(100):
        a[i] = list(map(int, input().split()))
    for i in range(len(a)):
        garo = 0
        dagag = 0
        dagag2 = 0
        for j in range(len(a[i])):
            garo += a[i][j]
            if max_sum < garo:  # if문이 for 안에 있어
                max_sum = garo  # i행의 모든 열이 다 max에 추가된다
            max_list.append(max_sum)
            if i == j:
                dagag += a[i][j]
                max_list.append(dagag)
            if i+j == 99:
                dagag2 += a[i][j]
                max_list.append(dagag2)

    for j in range(len(a[0])):
        sero = 0
        for i in range(len(a)):
            sero += a[j][i]
            if max_sum < sero:
                max_list.append(sero)
    print(max(max_list))



########################################################################### 영진코드
#
# T = 10
#
# for test_case in range(1, T + 1):
#     N = input()
#     arr = [[0 for _ in range(100)] for _ in range(100)]
#     for i in range(100):
#         arr[i] = list(map(int, input().split()))
#
#     max = -987654321
#     # 행
#     for x in range(len(arr)):
#         sum = 0
#         for y in range(len(arr[x])):
#             sum += arr[x][y]
#         if max < sum:
#             max = sum
#     # 열
#     for y in range(len(arr[0])):
#         sum = 0
#         for x in range(len(arr)):
#             sum += arr[x][y]
#         if max < sum:
#             max = sum
#     # 대각선 1
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i][i]
#         if max < sum:
#             max = sum
#     # 대각선 2
#     for i in range(-1, len(arr), -1):
#         sum += arr[i][i]
#         if max < sum:
#             max = sum
#     print(f'#{test_case} {max}')

####################################################
# for t in range(10):
#     h, v, d1, d2 = 0, 0, 0, 0
#     tc = int(input())
#     data = [list(map(int, input().split())) for j in range(100)]
#     for x in range(100):
#         h = max(h, sum(data[x])) #각 행의 합
#         v = max(v, sum([data[t][x] for t in range(100)]))  #각 열의 합
#         d1 += data[x][x]
#         d2 += data[x][99-x]
#     print(f'#{tc} {max(h, v, d1, d2)}')