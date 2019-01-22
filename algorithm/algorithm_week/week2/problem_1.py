import sys
sys.stdin = open("problem_1.txt", 'r')
def printlist(a):
    for i in range(10):
        for j in range(10):
            print(a[i][j], end=' ')
        print()


T = int(input())
# print(T)
for test_case in range(1, (T + 1)):
    N = int(input())
    a = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for i in range(N):
        row_start, column_start, row_end, column_end, color_code = map(int, input().split())
        for j in range(row_start, row_end + 1):
            for k in range(column_start, column_end + 1):
                # if color_code != a[j][k]:
                a[j][k] += color_code
                if a[j][k] == 3:
                    cnt += 1
    print(f'#{test_case} {cnt}')

    # cnt = 0                                       #강사님 코드
    # for i in range(10):                           # 궁금한점1 : 왜 내코드는 오류가 발생하지 않는데 오답이 발생하나
    #     for j in range(10):                       # 궁금한점2 : 왜 값이 4인것은 없지?
    #         if a[i][j] == 3:
    #             cnt += 1
    # print(f'#{test_case} {cnt}')
