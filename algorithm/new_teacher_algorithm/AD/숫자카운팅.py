import sys
sys.stdin = open("숫자카운팅.txt")

def lowerSerch(s,e,f):
    sol = -1
    while s <=e:
        m = (s+e)//2
        if f == data[m]:
            sol = m
            e = m-1
        elif f >data[m]:
            s = m + 1
        elif f < data[m]:
            e = m-1
    return sol

def upperSerch(s,e,f):
    sol = -1
    while s <=e:
        m = (s + e) // 2
        if f == data[m]:
            sol = m
            s = m+1
        elif f > data[m]:
            s = m + 1
        elif f < data[m]:
            e = m-1
    return sol
N = int(input())
data = list(map(int, input().split()))
fN = int(input())
fdata = list(map(int, input().split()))

for i in range(fN):
    lo = lowerSerch(0,fN-1,fdata[i])
    if lo >= 0 :
        up = upperSerch(0, N-1, fdata[i])
        print(up-lo + 1, end=" ")
    else:
        print(0, end=" ")