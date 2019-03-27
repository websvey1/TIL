import sys
sys.stdin = open("달팽이사각형.txt")
N = int(input())
data = [[0 for i in range(N)]for j in range(N)]
# print(data)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
dno = 0
cnt = 0
a,b = 1,1

for i in range(N):
    data[i].append(-1)
    data[i].insert(0,-1)
data.append([-1] * (N+2))
data.insert(0, [-1] * (N+2))
print(data)
if N == 1:
    data[a][b] = 1
else:
    while cnt < (N*N):

        cnt += 1
        data[a][b] = cnt
        if data[a+dx[dno]][b+dy[dno]] == 0:
            a = a+dx[dno]
            b = b+dy[dno]
        elif data[a+dx[dno]][b+dy[dno]] < 0:
            cnt -=1
            dno = (dno+1)%4
        else:
            dno = (dno+1)%4
            a = a + dx[dno]
            b = b + dy[dno]



for i in range(1,N+1):
    print(*data[i][1:-1])


##################################### 강사님코드
# N = int(input())
# arr = [[0] * N for _ in range(N)]
#
# r, c = 0, -1  # 한칸 이전위치에서 시작
# num = 0  # 카운팅할 숫자
# cnt = N  # 루프 회전수
# while cnt !=0:
#     # 오른쪽방향
#     for i in range(cnt):
#         c += 1  # 열좌표만 증가하면서 오른방향으로
#         num += 1
#         arr[r][c] = num
#     cnt -= 1  # 회전수 1개 줄임
#     # 아래 방향
#     for i in range(cnt):
#         r += 1  # 열좌표만 증가하면서 오른방향으로
#         num += 1
#         arr[r][c] = num
#     # 왼쪽방향
#     for i in range(cnt):
#         c -= 1  # 열좌표만 증가하면서 오른방향으로
#         num += 1
#         arr[r][c] = num
#     cnt -= 1  # 회전수 1개 줄임
#     # 위쪽방향
#     for i in range(cnt):
#         r -= 1  # 열좌표만 증가하면서 오른방향으로
#         num += 1
#         arr[r][c] = num
#
# for i in range(N):
#     for j in range(N):
#         print(arr[i][j], end=' ')
#     print()