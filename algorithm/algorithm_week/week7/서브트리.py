def preorder(node):
    global cnt
    if node != 0:
        # print("{}".format(node), end=" ")
        cnt += 1
        preorder(p1[node])
        preorder(p2[node])

import sys
sys.stdin = open("서브트리.txt")

T = int(input())
for tc in range(1, T+1):
    M,N = map(int, input().split())
    data = list(map(int,input().split()))
    # print(data)
    # par = []
    p1 = [0 for _ in range(len(data))]
    p2 = [0 for _ in range(len(data))]
    cnt = 0
    for i in range(0, len(data) ,2):
        if p1[data[i]] == 0:
            p1[data[i]]= data[i+1]
        else:
            p2[data[i]]= data[i+1]
    print(p1)
    print(p2)
    preorder(N)
    print('#%d %d' %(tc,cnt))




