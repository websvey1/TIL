import sys
sys.stdin = open('최소신장트리.txt')

def prim(data,s):
    global V
    key = [float('inf')] * (V+1)
    pi = [0] * (V+1)
    visited = [0] * (V+1)
    key[s] = 0
    for _ in range(V+1):
        minindex = -1
        minn = float('inf')
        for i in range(V+1):
            if not visited[i] and key[i] <minn:
                minn = key[i]
                minindex = i
        visited[minindex] = 1
        for v, val in enumerate(data[minindex]):
            if not visited[v] and val < key[v]:
                key[v] = val
                pi[v] = minindex


T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())    # V+1개의 노드 E개의 간선
    data = [list(map(int, input().split()))for _ in range(E)]
    data.sort(key=lambda x:x[2])
    p = list(range(V+1)) # make_Set
    result = prim(data, 0)
    # print(data)
    # print(p)
    print(result)
    # print('#%d %d' %(tc,result))
