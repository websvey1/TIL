import sys
sys.stdin = open('뿌요뿌요.txt')
# def bomb():

def check(x,y):
    global RR, GG, BB, PP, YY
    if re_data[x][y] == 'R': RR += 1
    if re_data[x][y] == 'G': GG += 1
    if re_data[x][y] == 'B': BB += 1
    if re_data[x][y] == 'Y': YY += 1
    if re_data[x][y] == 'P': PP += 1
    return RR,GG,BB,YY,PP
def clean():
    # recover = [[0 for _ in range(12)]for _ in range(6)]

    for iii in range(6):
        FFF = 0
        recover = []
        real = ['.'] * 12
        for j in range(12):
            if re_data[iii][j] != '.':
                FFF = 1
                recover.append(re_data[iii][j])
        if FFF:
            for k in range(len(recover)):
                if real[k] =='.':
                    real[k] = recover[k]
        re_data[iii] = real
    bfs()  # 이거 인덴테이션 주의하가ㅣ.....

def bfs():
    global cnt
    F = 0
    for i in range(6):
        for j in range(12):
            if re_data[i][j] in ['R','G','B','Y','P']:
                que = []
                dx = (0,0,-1,1)
                dy = (-1, 1, 0,0)
                visit = []
                que.append((i, j))
                visit.append((i,j))
                while que:
                    x,y = que.pop(0)

                    for k in range(len(dx)):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if nx<0 or ny<0 or nx>=6 or ny>=12:continue
                        if re_data[nx][ny] != re_data[x][y] or (nx, ny) in visit: continue


                        que.append((nx,ny))
                        visit.append((nx,ny))
                LEN = int(len(visit))
                if LEN>=4:
                    F = 1
                    for V in range(len(visit)):
                        VX, VY = visit.pop()
                        re_data[VX][VY] = '.'

    if F:
        cnt +=1
        clean()

    else:
        return

T = int(input())
for tc in range(1,T+1):
    data = [list(input())for _ in range(12)]
    re_data = [[0 for _ in range(12)]for _ in range(6)]
    for i in range(12):
        for j in range(6):
            re_data[j][i] = data[11-i][j]

    for i in range(6):
        print(*re_data[i])
    print()
    cnt = 0
    bfs()
    for i in range(6):
        print(*re_data[i])
    print(cnt)