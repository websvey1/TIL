# M,N = map(int, input().split())
M,N = 4,4
# data = [ list(map(int, input().split())) for _ in range(M) ]
data = [[0, 1, 0, 0], [1, 1, 0, 1], [1, 0, 1, 0], [1, 1, 1, 0]]

for i in range(M):
    for j in range(1, N):
        if data[i][j] !=0:
            if data[i][j-1] !=0:
                data[i][j] += data[i][j-1]
# print(data)
for T in range(M):
    for Y in range(N):
        print(data[T][Y], end=" ")
    print()