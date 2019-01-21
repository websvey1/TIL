import sys
sys.stdin = open("min_max_input.txt")

T = int(input())

for n in range(1, T+1):
    num = int(input())
    num_list = list(map(int, input().split()))

    for i in range(len(num_list)-1, 0, -1):
        for j in range(i):
            if num_list[j] < num_list[j+1]:
                num_list[j],  num_list[j+1] = num_list[j+1],  num_list[j]

    print(f'#{n} {num_list[0] - num_list[-1]}')


    ############################################
    import sys
sys.stdin = open("bus_input.txt")

T = int(input())

for n in range(1, T + 1):
    K, N, M = map(int, input().split())
    route = list(map(int, input().split()))
    charge_route = [0] * (N + K)
    charge_route[N] = 1

    for i in route:
        charge_route[i] = 1
    count = 0
    point = K

    while True:
        if charge_route[point] != 1:
            point += -1
        elif charge_route[point] == 1:
            count += 1
            charge_route = charge_route[point:]
            point = K
            if len(charge_route) == K:
                count += -1
                break

        if point == 0:
            count = 0
            break
    print(f'#{n} {count}')

    ##########################################
    
import sys
sys.stdin = open("numcard_input.txt")

N = int(input())

for T in range(1, N+1):
    num = int(input())
    nums = list(map(int, input()))
    cnt_list = [0] * 10

    for i in nums:
        cnt_list[i] += 1
    count_num = cnt_list[0]

    for i in range(1, len(cnt_list)):
        if count_num <= cnt_list[i]:
            result_num = i
            count_num = cnt_list[i]

    print(f'#{T} {result_num} {count_num}')

    #############################################
    import sys
sys.stdin = open("Flatten_input.txt")


for n in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    cnt = 0
    boxes_num = boxes[0]
    for T in range(N):
        for i in range(len(boxes)):
            if boxes_num < boxes[i]:
                boxes_num = boxes[i]
                boxes_number = i
        boxes[boxes_number] += -1

        for i in range(len(boxes)):
            if boxes_num > boxes[i]:
                boxes_num = boxes[i]
                boxes_number = i
        boxes[boxes_number] += 1

    max_num = boxes[0]
    for i in range(len(boxes)):
        if max_num < boxes[i]:
            max_num = boxes[i]

    min_num = boxes[0]
    for i in range(len(boxes)):
        if min_num > boxes[i]:
            min_num = boxes[i]

    result = max_num - min_num
    print(f'#{n} {result}')