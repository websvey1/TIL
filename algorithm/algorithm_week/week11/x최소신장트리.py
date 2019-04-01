import sys
sys.stdin = open('최소신장트리.txt')
def make_Set(v):
    global p
    p[v] = v
def find_Set(n):  # n의 부모노드를 구하는 함수
    if n==p[n] : return n
    else: return find_Set(p[n])




def kruskal():
    global V
    c,s,i = 0,0,0
    while c<V:               #mst 구성을 위해 v개의 간선을
        p1 = find_Set(data[i][0])  # 앞 정점의 부모를 구함
        p2 = find_Set(data[i][1])  # 뒷 정점의 부모를 구함
        if p1 != p2:               # 부모가 다를때 합을 구함.
            s += data[i][2]
            c +=1 #  정점의개수 V
            p[p2] = p1      # union(p1, p2)
        i +=1
        # else: 점점p1과 p2의 부모가 같을 경우= cycle이므로 pass
    return s



T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())    # V+1개의 노드 E개의 간선
    data = [list(map(int, input().split()))for _ in range(E)]
    data.sort(key=lambda x:x[2])
    p = list(range(V+1)) # make_Set
    result = kruskal()
    # print(data)
    # print(p)
    print('#%d %d' %(tc,result))
