import sys
sys.stdin = open("폭탄돌리기.txt")

time = 210
mem = [1,2,3,4,5,6,7,8]

start = mem[mem.index(int(input()))]
quiz = int(input())
cnt = 0

for q in range(quiz):
    data_time, data_value = input().split()
    data_time = int(data_time)

    time -= data_time
    if time <0:
        break
    if data_value == "T":
        start += 1
        if start >8:
            start %= 8
print(start)