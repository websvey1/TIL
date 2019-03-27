import sys
sys.stdin = open("미로탈출로봇.txt")
def BFS():
    que = []
    time = 0
    dx = (0,0,-1,1)
    dy = (-1,1,0,0)
    que.append((sc,sr,time))
    data[sc][sr] = 1
    while que:
        c,r,time = que.pop(0)
        if c == ec and r == er: return time
        for i in range(4):
            nc = c+dx[i]
            nr = r+dy[i]
            if nc < 0 or nr < 0 or nc >= C or nr >= R:continue

            if data[nc][nr] !=0:continue
            que.append((nc,nr,time+1))

            data[nc][nr] = 1
    return -1


R,C = map(int, input().split())
sr,sc,er,ec = map(int, input().split())
data = [list(map(int, input()))for _ in range(C)]
print(data)
sr -=1; sc -=1; er -=1; ec -=1;
a = BFS()
print(a)




























#
# def BFS():
#     que = []
#     dr = (-1,1,0,0) #
#     dc = (0,0,-1,1)
#     que.append((sr,sc,0)) # 시작점
#     arr[sr][sc] = 1 # 시작 visit표시
#     while que: # 큐가 있을때 반복
#         r,c,time = que.pop(0) # 큐에서 데이터 읽기
#         if r==er and c ==ec : return time
#         for i in range(4): # 델타검색
#             nr = r+dr[i]
#             nc = c+dc[i]
#             if nr < 0 or nr>=R or nc<0 or nc>=C: continue # 범위
#             if arr[nr][nc] != 0 : continue # 길이아니면 스팁
#             que.append((nr,nc,time+1))
#             # print(que)
#             arr[nr][nc] = 1 # 방문표시
#     return -1
# C,R = map(int, input().split())
# sc,sr,ec,er = map(int,input().split())
# sc-=1
# sr-=1
# ec-=1
# er-=1
# arr = [list(map(int, input())) for _ in range(R)]
# print(arr)
# 값 = BFS()
# print(값)