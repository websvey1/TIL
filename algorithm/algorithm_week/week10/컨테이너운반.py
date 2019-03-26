import sys
sys.stdin = open('컨테이너운반.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    container = sorted(list(map(int, input().split())))
    truck = sorted(list(map(int, input().split())))
    carry = [ 0 for _ in range(len(truck))]
    move = 0
    i,j =  len(container)-1, len(truck)-1
    # print(i,j)
    # print(container, truck)

    # for i in range(len(container)):
    #     for j in range(len(truck)):
    #         if truck[j] >= container[i] and carry[j] < container[i]:
    #             carry[j] = container[i]
    #         print(i,j, end="  ")
    #         print(carry)
    #
    # print(sum(carry))
    while j >=0 and i >=0:
        if container[i] <= truck[j]:
            carry[j] = container[i]
            j -= 1
            i -= 1
        elif container[i] > truck[j]:
            i -= 1
    print(sum(carry))