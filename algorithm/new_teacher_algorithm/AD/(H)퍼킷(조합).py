import sys
sys.stdin = open('퍼킷.txt')

재료 = int(input())
맛 = [list(map(int,input().split()))for _ in range(재료)]
비교()