import sys, time
start = time.time()
sys.stdin = open("./tc/set_calc.txt","r")

T = int(input())
for tc in range(T):
    L,M = map(int, input().split())
    data = list(map(int, input().split()))
    # print(data)
    MIN = float('inf')
    MAX = 0

    for i in range(L-(M-1)):
        if sum(data[i:i+M]) <MIN:
            MIN = sum(data[i:i+M])
        if sum(data[i:i+M]) > MAX:
            MAX = sum(data[i:i+M])
        # tmp = 0
        # for j in range(i,i+M):
        #     tmp += data[j]
        # if tmp < MIN:
        #     MIN = tmp
        # if tmp > MAX:
        #     MAX = tmp
        # print(tmp)

    print("#%d %d" %(tc+1,MAX-MIN))
    print('time: ', time.time() - start)