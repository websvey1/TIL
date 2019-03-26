def isWall(i,j):
    if i<0 or N <=i or j<0 or N<=j:
        return False
    else:
        return True
def find(i,j,hap):
    global result
    if i == N-1 and j == N-1:
        hap += data[i][j]
        result = min(result, hap)
        hap = 0
        return

    elif isWall(i,j):
        hap +=data[i][j]
        find(i,j+1,hap)
        find(i+1,j,hap)

import sys
sys.stdin = open("최소합.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int, input().split()))for _ in range(N)]
    i,j = 0,0
    result = 99999999
    hap = 0
    find(i,j,hap)
    print('#%d %d' %(tc,result))
