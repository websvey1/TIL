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
    while c<V:               #mst 구성을 위해 v개의 간선을 t선택(점이 5개이므로 간선이 4개여야 MST가 됨
        p1 = find_Set(data[i][0])  # 앞 정점의 부모를 구함
        p2 = find_Set(data[i][1])  # 뒷 정점의 부모를 구함
        if p1 != p2:               # 부모가 다를때 합을 구함.
            s += data[i][2]
            c +=1 #  정점의개수를 카운트 하는 변수, V와 같아지면 while문이 끝난다.
            p[p2] = p1      # union(p1, p2) / p1 p2의 부모가 다르면 p2의 부모를 p1의 부모로 변경
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
    print(data)
    print(p)
    print('#%d %d' %(tc,result))

###################################################################################
########################## 위 : 클루스칼, 아래  : 프림 ################################
###################################################################################
# def mst():
#     global V
#     total = 0
#     u = 0 # 시작점.(u 에 접한 접점을 비교한다)
#     D[u] = 0 # 무한대를 0으로 초기화
#     PI[u] = 0 # 부모를 0 으로 초기화
#                                          ################################
#     for i in range(V+1):
#         mmiinn = float('inf') # 가중치 최소값 찾기
#         for v in range(V+1):
#             if visit[v] == 0 and mmiinn > D[v]:  # 이부분이 시간이 많이걸림 / 방문 안한것 찾고, 가중치가 min보다 작은건ㅅ
#                 mmiinn = D[v]
#                 u = v
#                                         ################################
#         visit[u] = 1
#         total += adj[PI[u]][u]
#
#         for v in range(V+1): # 인접한 정점v 업데이트
#             if adj[u][v] != 0 and visit[v] == 0 and adj[u][v] < D[v]: # 다음 정점v가 u에서 갈 수 있고, 방문한적 없으며, 그값이 가중치 D보다 작을때,
#                 D[v] = adj[u][v]  # 가중치와 부모를 갱신
#                 PI[v] = u
#     return total
#
# T = int(input())
# for tc in range(1,T+1):
#     V, E = map(int, input().split())    # V+1개의 노드 E개의 간선
#     adj = [[0] *(V+1) for _ in range(V+1)]
#     D = [float('inf')]*(V+1)
#     PI = list(range(V+1)) # 부모 = 자기 자신 인덱스르 값으로 갖음
#     visit = [0] * (V+1)
#     for i in range(E):
#         data = list(map(int, input().split()))
#         for j in range(len(data)):
#             adj[data[0]][data[1]] = data[2]
#             adj[data[1]][data[0]] = data[2]
#
#
#     print('#%d %d' %(tc,mst()))
#     # print(PI)