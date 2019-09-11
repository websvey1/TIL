import sys
sys.stdin = open("./tc/num_card.txt", "r")

N = int(input())
for tc in range(N):
    leng = int(input())
    data = input()
    arr = [0] * 10
    result = 0
    mem = 0
    for i in range(len(data)):
        arr[int(data[i])] += 1
    for i in range(len(arr)):
        if arr[i] >= result:
            result = arr[i]
            mem = i
    print("#%d %d %d" %((tc+1),mem, result))
