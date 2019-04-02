import sys
sys.stdin = open('건물세우기.txt')

def perm(x,y,hap):
    global result
    if x == y:
        if hap < result:
            result = hap
        return
    else:
        for i in range(x,y):
            a[i],a[x] = a[x],a[i]
            if hap+data[x][a[x]] < result:
                perm(x+1, y, hap+data[x][a[x]])
            a[i], a[x] = a[x], a[i]

N = int(input())
data = [list(map(int, input().split()))for _ in range(N)]
result = float('inf')
a = list(range(N))
perm(0,N,0)
print(result)
