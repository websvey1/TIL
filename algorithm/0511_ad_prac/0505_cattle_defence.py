import sys
sys.stdin = open('0505_cattle_defence.txt')

def jeok():  #(3) 적의 위치를 찾아 리스트를 만드는 함수
    tmp_data = data[:]
    for_kill_list = []
    for i in range(N):
        for j in range(M):
            if tmp_data[i][j] == 1:
                for_kill_list.append((i,j))
    return tmp_data, for_kill_list

def bfs(ar):    #(2) 궁수의 위치에서 적을 공격하는 함수
    kill = 0
    F = 1
    # a1,a2,a3 = ar
    tmp_data, k_list = jeok()
    # print(k_list)
    for i in range(len(k_list)):
        for j in range(len(ar)):
            if abs(N-(k_list[i][0])) + abs(ar[j]-(k_list[i][1])) <= D:   # 궁수의 사거리에 닿이면 죽이는 함수
                kill += 1                                               # 죽인후 적이 잇던 자리를 0으로 치환
                tmp_data[k_list[i][0]][k_list[i][1]] = 0
                                                            #이 다음에 적이 있나 검사를 하고,사거리를 증가 ? X
                                                            # 사거리를 늘린 후 적이 있나 검사
    for i in range(N):                       # 데이터가 모두 0이면 리턴하기 위한 함수
        for j in range(M):
            if tmp_data[i][j] == 1:
                F = 0
    if F:                             # 디버깅 해봐야할부분,., 이상하게 돈다
        print(kill)
        print(tmp_data)
        return


def arrow(n,k):  #(1) 궁수의 자리를 배치하는 함수.
    if k == 3:
        print(visit)
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



# 내리는 함수 or 사거리 증가시키는 함수가 없음.
# 죽인수 kill을 어디에 저장할지와,
