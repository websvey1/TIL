def find_T(c,C):
    T = []
    for i in range(c,C+1):
        for j in range(c,C+1):
            if i<j:
                T.append([i,j])
    return list(T)
import sys
sys.stdin = open("반나누기.txt")

T = int(input())
for tc in range(1, T+1):
    N, m, M = map(int, input().split())
    score = list(map(int, input().split()))
    # print(score)
    C = max(score)
    c = min(score)
    X = find_T(c,C)
    MMIINN = 999999999
    print(X)

    for i in range(len(X)):
        c_a, c_b, c_c = 0, 0, 0
        T1, T2= X[i][0], X[i][1]
        # print("T1, T2", T1, T2)
        for j in range(len(score)):
            if score[j] < T1:
                c_c+=1
            elif T1<=score[j] < T2:
                c_b+=1
            else:
                c_a+=1
        if c_a !=0 and c_b!=0 and c_c !=0 and max(c_a,c_b,c_c) <=M and min(c_a,c_b,c_c) >= m:
            empty = [c_a,c_b,c_c]
            if MMIINN > max(empty) - min(empty):
                MMIINN = max(empty) - min(empty)
            print(empty)
    if MMIINN == 999999999:
        print(-1)
    else:
        print(MMIINN)