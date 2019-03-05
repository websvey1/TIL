import sys
sys.stdin = open("이진탐색.txt")
def inorder(node):
    global ho, N
    if node <= N:
        inorder(node*2)
        Q[node] = ho
        ho +=1
        inorder(node*2+1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Q = [0 for _ in range(N + 1)]
    ho = 1
    inorder(1)
    # print(Q)
    print('#{} {} {}'.format(tc, Q[1], Q[N//2]))