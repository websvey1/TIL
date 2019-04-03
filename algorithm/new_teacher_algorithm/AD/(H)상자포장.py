import sys
sys.stdin = open('상자포장.txt')
def dfs(x,a,b,hap):
    if x == N:

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = list(map(int, input().split()))
    A,B = [1000],[0]
    hap = 0
    dfs(data[0],A[-1],B[-1],hap)