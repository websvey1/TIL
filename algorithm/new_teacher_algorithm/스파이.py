import sys
sys.stdin = open("스파이.txt")

N, data = input().split()
cnt = 0
result = []
flag = 0
i = 0
while i < len(data):
    if data[i] == '<':  # 증가
        cnt +=1
        i +=1
    elif data[i] == '>': # 감소
        cnt -=1
        i +=1
    else:  # 숫 자 일 때
        flag = i
        while data[i] !='<' or data[i] != '>':
            # result.append([cnt, int(data[i])])
            i += 1
            if data[i] == '<' or data[i] == '>':
                result.append([cnt, int(data[flag:i])])
                print(result)
                break

print(result)
# print(N)
for j in range(len(result)):
    if result[j][0] == int(N):
        print(result[j][1], end = " ")
