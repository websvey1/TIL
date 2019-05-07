import sys
sys.stdin = open('문자테트리스.txt')

T = int(input())
for tc in range(1,T+1):
    data = list(map(str, input()))
    # print(data)
    i = 1
    while i < len(data):
        if data[i] == data[i-1]:
            del data[i]
            del data[i-1]
            i = 1
        else:
            i +=1
    # print(data)
    print(len(data))