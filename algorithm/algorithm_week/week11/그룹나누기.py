import sys
sys.stdin = open('그룹나누기.txt')

def find_Set(n):  # n의 부모노드를 구하는 함수
    if n==p[n] : return n
    else: return find_Set(p[n])

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    data = list(map(int, input().split()))
    cnt = 0
    p = list(range(N+1))
    for i in range(M):
        p1 = find_Set(data[i*2])
        p2 = find_Set(data[i*2+1])
        if p1 != p2:
            p[p2] = p1
    result = 0
    for i in range(1,len(p)):
        if i == p[i]:
            result +=1
    print('#%d %d' %(tc,result))

