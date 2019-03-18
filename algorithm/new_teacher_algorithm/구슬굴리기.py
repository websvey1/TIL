def find(data):
    for i in range(len(data)):
        if 2 in data[i]:
            return i, data[i].index(2)
import sys
sys.stdin = open("구슬굴리기.txt")
R,C = map(int, input().split())

data = [list(map(int, input())) for _ in range(C)]
for i in range(len(data)):
    data[i].append(1)
    data[i].insert(0,1)
data.append([1]*(R+2))
data.insert(0, [1]*(R+2))

N = int(input())
move = list(map(int, input().split()))
# print(move)
x,y = find(data)

flag = 0
cnt = 1
dy = [0,0,0,-1,1]
dx = [0,-1,1,0,0]


while data[x][y] !=0 and flag < N:
    if data[x+dx[move[flag]]][y+dy[move[flag]]] == 0:
        data[x + dx[move[flag]]][y + dy[move[flag]]] = 9
        x = x+dx[move[flag]]
        y = y+dy[move[flag]]
        cnt += 1

    elif data[x+dx[move[flag]]][y+dy[move[flag]]] == 1:
        flag += 1
    elif data[x+dx[move[flag]]][y+dy[move[flag]]] == 9:
        x = x+dx[move[flag]]
        y = y+dy[move[flag]]
    elif data[x+dx[move[flag]]][y+dy[move[flag]]] == 2:
        x = x+dx[move[flag]]
        y = y+dy[move[flag]]
print(cnt)
# for i in range(len(data)):
#     print(*data[i])