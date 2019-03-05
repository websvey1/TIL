def searchAnce(n):
    s = tree[n][2]
    p = []
    while s!=0:
        p.append(s)
        s = tree[s][2]
    return p

def findA(p1,p2):
    for i in range(len(p1)):
        for j in range(len(p2)):
            if p1[i] == p2[j]:
                return p1[i]
    return 0

def preorder(node):
    global cnt
    if node !=0:
        # print("{}".format(node), end=" ")
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

import sys
sys.stdin = open("공통조상.txt")

T = int(input())
for tc in range(T):
    V, E, n1, n2 = map(int, input().split())
    tree = [[0 for _ in range(3)] for _ in range(V+1)]
    temp = list(map(int, input().split()))
    p1 = []
    p2 = []
    cnt = 0
    for i in range(E):
        p = temp[i*2]
        c = temp[i*2+1]
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c

        tree[c][2] = p
