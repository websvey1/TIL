import sys
sys.stdin = open('양팔저울.txt')
def dfs(no,L,R):
    global sol
    if sol:return # 가지치기
    if no==CN:
        if L == R:
            sol = 1
        return
    else:
        dfs(no+1, L, R) # 미사용
        dfs(no+1, L+chu[no], R) # 추를 왼쪽에
        dfs(no+1, L, R+chu[no])  # 추를 오른쪽에
CN = int(input())
chu = list(map(int, input().split()))
BN = int(input())
ball = list(map(int, input().split()))
rec = [0] * CN
for i in range(BN):
    sol = 0
    dfs(0, ball[i], 0) #0번추 부터 시작, 왼쪽저울무게를 구슬무게로 초기값으로, 오른저울무게0
    if sol:print('Y', end=" ")
    else: print('N', end=" ")