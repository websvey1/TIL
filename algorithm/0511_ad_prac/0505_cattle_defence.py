import sys
sys.stdin = open('0505_cattle_defence.txt')
def jeok():
    tmp_data = data[:]
    for_kill_list = []
    for i in range(N):
        for j in range(M):
            if tmp_data[i][j] == 1:
                for_kill_list.append((i,j))
    return tmp_data, for_kill_list
def bfs(ar):

    # a1,a2,a3 = ar
    tmp_data, k_list = jeok()
    print(k_list)
    for i in range(len(k_list)):
        for j in range(len(ar)):
            if abs(N-(k_list[i][0])) + abs(ar[j]-(k_list[i][1])) <= D:
                tmp_data[k_list[i][0]][k_list[i][1]] = 0


def arrow(n,k):
    if k == 3:
        # print(visit)
        # a1,a2,a3 = visit
        bfs(visit)
        return
    if n == M:
        return
    else:
        visit[k] = all_arrow[n]
        arrow(n+1, k+1)
        visit[k] = 0
        arrow(n+1,k)


N,M,D = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
all_arrow = list(range(M))

print(all_arrow)
visit = [0] * 3
arrow(0,0)
