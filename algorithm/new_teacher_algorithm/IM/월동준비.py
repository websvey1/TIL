import sys
sys.stdin = open("월동준비.txt")

T = int(input())
data = list(map(int, input().split()))
max_num = 0
smart = 0
comp = 0
for i in range(T):
    if data[i]+comp <0:
        comp = 0
    else:
        if data[i]+comp > max_num:
            max_num = data[i]+comp
        comp = data[i]+comp
    print(max_num, comp)
for i in range(T):
    if data[i]>0:
        smart += data[i]
if max_num >0 and smart >0:
    print(max_num, smart)
else:
    print(max(data), max(data))