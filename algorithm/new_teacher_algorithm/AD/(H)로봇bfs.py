import sys
sys.stdin = open('로봇.txt')
def bfs()
    dr = (0,0,0,1,-1)
    dc = (0,1,-1,0,0)
    turn =  [(0,0),(4,3),(3,4),(1,2),(2,1)] #동서남북
    que = []
    while que:
        for i in range(1,4): # go 1,2,3

        for i in range(2): #turn left, right
R,C = map(int, input().split())
data = [list(map(int, input().split()))for _ in range(R)]
arr = [[[0]*C for i in range(R)]for j in range(5)]
sr,sc,sd = map(int, input().split())
er,ec,ed = map(int, input().split())
result = bfs()
print(result)