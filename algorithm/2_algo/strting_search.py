import sys, time
start = time.time()
sys.stdin = open("./tc/strting_search.txt","r")

T = int(input())
for tc in range(1,T+1):
    data = input()
    all = input()
    ############# 쉬운버전 ############3  0.0초
    result = 5
    if data in all:
        result = 1
    else:
        result = 0

    ###############3 어렵 ####################3  0.001초
    # result = 5
    #
    # for i in range(len(all)-len(data)+1):
    #     if all[i:i+len(data)] == data:
    #         result = 1
    #         break
    #     else:
    #         result = 0
        # print(data)
        # print(all[i:i+len(data)])

    print("#%d %d" %(tc,result), time.time()- start)
