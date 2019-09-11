import sys
sys.stdin = open("./tc/search_binary.txt", "r")

N = int(input())
for tc in range(1,N+1):
    def chk():
        global cnt_a, cnt_b
        if cnt_a > cnt_b:
            return 'B'
        if cnt_a < cnt_b:
            return 'A'
        else:
            return '0'
    all,a,b = map(int, input().split())
    s = 1
    e = all
    m = 0
    cnt_a = 0
    while a!=m and m != e-1:
        m = (s+e)//2
        cnt_a +=1
        if a>m:
            s = m
        if a<m:
            e = m
    # print(m)
    s = 1
    e = all
    m = 0
    cnt_b = 0
    while b!=m and m != e-1:
        m = (s+e)//2
        cnt_b +=1
        if b>m:
            s = m
        if b<m:
            e = m
    # print(m)
    # print(cnt_a,cnt_b)
    RR = chk()
    print("#%d %s" %(tc, RR))