import sys
sys.stdin = open("problem_2.txt")

def find_start(A):
    for i in range(len(A)):
        if 2 in A[i]:
            return i, A[i].index(2)

def find_end(a,b):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(len(dx)):
        if a+dy[i] >= 0 and a+dy[i] < N and b+dx[i] >=0 and b+dx[i] <N:
            if data[a+dy[i]][b+dx[i]] == 1:
                continue
            elif data[a+dy[i]][b+dx[i]] == 3:
                data[a][b] = 9
                a, b = a + dy[i], b + dx[i]
                # return a+dy[i], b+dx[i]
                # print('check')
                return 1

            elif data[a + dy[i]][b + dx[i]] == 0:
                data[a][b] = 9
                a,b = a+dy[i], b+dx[i]
                # print(f'{tc}, 1')
                return find_end(a,b)





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    print(data)
    a, b = find_start(data)
    print(find_end(a,b))