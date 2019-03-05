import sys
sys.stdin = open("이진힙.txt")

def enQ(n):
    global last
    last +=1
    c = last
    p = c // 2
    Q[last] = n
    while c > 1 and Q[p] > Q[c]:
        t = Q[p]
        Q[p] = Q[c]
        Q[c] = t
        c = p
        p //= 2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))

    last = 0
    Q = [0 for _ in range(len(data)+1)]

    for i in range(len(data)):
        enQ(data[i])

    result = 0
    t = len(Q)-1
    # print('Q', Q)
    while t !=0:
        result +=Q[t//2]
        t //= 2
    print('#%d %d' %(tc, result))


