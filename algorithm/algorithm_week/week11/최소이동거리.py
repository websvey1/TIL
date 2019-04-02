import sys
sys.stdin = open('최소이동거리.txt')

# T = int(input())
# for tc in range(1,T+1):
#     N,E = map(int, input().split())
#     data = [list(map(int, input().split()))for _ in range(E)]
#
#     arr = [[0] * (N+1) for _ in range(N+1)]
#
#     for i in range(N+1):
#         arr[data[i][0]][data[i][1]] = data[i][2]
#
#     D = [float('inf') for _ in range(N+1)]
#     visited = [0 for _ in range(N+1)]
#
#     cnt = 0
#     D[cnt] = 0
#
#
#     while cnt<N:
#         visited[cnt] = 1
#         for i in range(len(data)):
#             p1 = data[i][0]
#             p2 = data[i][1]
#             if p1 == cnt and visited[p2]==0:
#                 D[p2] = min(D[p2], D[cnt]+arr[p1][p2])
#         result = float('inf')
#         for j in range(len(D)):
#             if visited[j] == 0 and D[j] < result:
#                 result = D[j]
#                 cnt = j
#     print(D)
#     print('#%d %d' %(tc,D[-1]))
###########################################################################
###########################################################################
def getMinIdx():
    minV = 999999  #
    minIdx = 0
    for i in range(N + 1):  # 방문 안 한 노드 중 D가 최소인 노드 찾기
        if visit[i] == 0 and D[i] < minV:  # 방문을 한 적이 없고, 가중치dㄱ 최소인 노드 찾기
            minIdx = i
            minV = D[i]
    return minIdx

def dijkstra(goal):
    D[0] = 0                #츌발점의 가중치

    for i in range(N+1):
        if adj[0][i]:        # 출발점과 인접한 노드에 가중치 입력
            D[i] = adj[0][i] # 초기화
    visit[0] = 1             #시작노드

    while True:
        node = getMinIdx()
        visit[node] = 1    #D가 가장 작은 노드 방문처리
        if node == goal:    #도착지에 도착하면
            return D[goal]

        for x in range(N+1):
            if adj[node][x]:   #인접행렬의 노드 x축 검사
                if D[x] > (D[node]+adj[node][x]):
                    D[x] = D[node]+adj[node][x]

T = int(input())
for tc in range(1,T+1):
    N,E = map(int, input().split())
    data = [list(map(int, input().split()))for _ in range(E)]
    print(data)
    adj = [[0] * (N+1) for _ in range(N+1)] #인접행렬
    # print(adj)
    for i in range(E):
        adj[data[i][0]][data[i][1]] = data[i][2]

    D = [float('inf') for _ in range(N+1)]
    visit = [0 for _ in range(N+1)]
    print(dijkstra(N))