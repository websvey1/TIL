import sys
sys.stdin = open("원안의사각형.txt")

R = int(input())
cnt = 0
for i in range(1,R+1):
    for j in range(1,R+1):
        if i**2 + j**2 <= R**2:
            cnt += 1
print(cnt*4)