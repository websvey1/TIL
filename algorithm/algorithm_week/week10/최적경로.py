def find():
    hap = 0
    global hap, result
    for i in range(0,len(data),2):
        if i ==0:
            hap += abs(data[i]-company[0])+ abs(data[i+1]-company[1])
            return
        if i == len(data)-2:
            hap += abs(data[i]-home[0])+ abs(data[i+1]-home[1])
        else:
            hap += abs(data[i]-data[i-2])+ abs(data[i+1]-data[i-1])
    if hap < result:
        result = hap


def perm(n,k):
    if n == k:
        find()
        # myprint(n)
    else:
        for i in range(k,n):
            data[i], data[k] = data[k], data[i]
            perm(n, k+1)
            data[i], data[k] = data[k], data[i]


import sys
sys.stdin = open("최적경로.txt")
T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    visit = [[0 for _ in range(100)] for _ in range(100)]
    company = data[:2:]
    home = data[2:4:]
    data = data[4::]
    result = 99999999999999
    hap = 0
    idx_list = [i for i in range(N)]
    perm(N,0)

    print(result, hap)



