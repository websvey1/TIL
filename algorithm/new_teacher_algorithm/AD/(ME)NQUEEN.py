def check(x,y):
    dx = [-1,-1,-1]
    dy = [-1, 0, 1]             #델타검색
    for i in range(len(dx)):
        for k in range(1,N):  #델타검색에다 배수 추가
            nx = x+dx[i]*k
            ny = y+dy[i]*k
            if nx<0 or ny<0 or nx>=N or ny>=N:continue #
            if data[nx][ny]==1: return 0
    return 1
def dfs(x,n):
    global result, hap1, hap2, hap3
    if x==n:
        result +=1
        return             #여기 return이 없으면 동작을 안한다.
    ####################### chkeck 함수 이용 ###################3
    # for i in range(N):
    #     if check(x,i):     #체크할 수 있으면,(퀸을 놓을 수 있으면,)
    #         data[x][i] = 1  # 그 열에 방문체크
    #         dfs(x+1,n)
    #         data[x][i] = 0  # 재귀가 풀리면서 방문해제
    ####################### chkeck 함수 이용 ###################3

    ####################### chkeck 배열 ###################3
    for i in range(N):
        if hap1[i]:continue
        if hap2[i+x]:continue
        if hap3[(N-1)-(x-i)]:continue
        hap1[i] = hap2[i+x] = hap3[(N-1)-(x-i)] = 1
        dfs(x+1,n)
        hap1[i] = hap2[i + x] = hap3[(N - 1) - (x - i)] = 0
N = 4
data = [[0 for i in range(N)]for _ in range(N)]
# print(data)
result = 0

hap1 = [0]*N
hap2 = [0]*(N*2)
hap3 = [0]*(N*2)
dfs(0,N)
print(result)