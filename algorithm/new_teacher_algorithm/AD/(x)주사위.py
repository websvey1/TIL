def dfs1(no): # 중복순열
    if no>N:
        for i in range(1+N+1): print(rec[i], end=" ")
        print()
        return
    for i in range(1,7):
        rec[no] = i
        dfs1(no+1)

def dfs3(no): #순열
    if no>N:
        for i in range(1+N+1): print(rec[i], end=" ")
        print()
        return
    for i in range(1,7):
        chk[i] = 1
        rec[no] = i
        dfs3(no+1)
        chk[i] = 0

def dfs2(no,s): # 중복조합, no번째 주사위가 선택한 시작하는 눈 s
    if no>N:
        for i in range(1+N+1): print(rec[i], end=" ")
        print()
        return
    for i in range(1,7):
        rec[no] = i
        dfs2(no+1,i)

def dfs4(no,s): # 조합, no번째 주사위가 선택한 시작하는 눈 s
    if no>N:
        for i in range(1+N+1): print(rec[i], end=" ")
        print()
        return
    for i in range(s,7):
        rec[no] = i
        dfs4(no+1,i+1)
N,M = map(int, input().split())
chk = [0] * N
rec = [0] * N
# if M==1: dfs1(1)
# if M==2: dfs2(1,1)
# if M==3: dfs3(1)