import sys, time
sys.stdin = open("./tc/str_num.txt", "r")
start = time.time()

T = int(input())
for tc in range(1,T+1):
    ############### 리스트 #################3
    fd = list(input())
    data = list(input())
    # print(fd)
    cnt = 0
    tmp = 0
    for i in range(len(fd)):
        # if cnt < data.count[fd[i]]:
        tmp = data.count(fd[i])
        # print(tmp)
        if cnt < tmp:
            cnt = tmp
    print("#%d %d" %(tc,cnt))
        # print(cnt)
