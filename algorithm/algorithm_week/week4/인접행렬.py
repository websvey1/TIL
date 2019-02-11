# 인접행렬
import sys
sys.stdin = open("인접행렬.txt", "r")

N, T = map(int, (input().split()))
N += 1
total = list(map(int, input().split()))

G = [[0 for i in range(N)] for j in range(N)]
visited = [0 for i in range(N)]
# print(total)
# for tc in range(1, T+1):

for i in range(0, len(total), 2):
    G[total[i]][total[i+1]] = 1
    G[total[i+1]][total[i]] = 1

for i in range(N):
    print(f'{i} {G[i]}')

# 인접행렬을 재귀로 ? 이거 안됌
def dfs(v):
    global G, visited, N
    visited[v] = 1
    print(v, end=" ")

    for w in range(N):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

dfs(1)



