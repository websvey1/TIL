import sys
sys.stdin = open("개구리.txt")

N = int(input())
data = sorted([int(input()) for i in range(N)])
cnt=0
# print(data)
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if data[j]-data[i] <= data[k]-data[j] and (data[j]-data[i])*2 >= data[k]-data[j]:
                # print(data[i],data[j],data[k])
                cnt+=1
print(cnt)