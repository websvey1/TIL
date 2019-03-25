data = [1,2,3,4,5,6,7,8,9,10]

count = 0
N = 10
A = [0 for _ in range(N)]
flag = 1
total = 0

def printSet(n):
    global count
    count +=1
    hap = 0
    for i in range(n):
        if A[i] == 1:
            hap += data[i]

    if hap >10: return
    if hap == 10:
        for i in range(n):
            if A[i] == 1:
                print("%d " % data[i], end="")
        print()


def powerset(n,k,hap): # n:원소갯수 k:현재 depth  가지치기 : hap변수 추가
    global total
    if hap >10: return    # 가지치기 추가부분
    total += 1
    if n == k:
        printSet(n)
    else:
        A[k] = 1   # k번요소 있음
        powerset(n, k+1, hap +data[k])   # 가지치기 뒤 추가
        A[k] = 0   # 없음
        powerset(n, k+1, hap)

powerset(N,0,0)     # 가지치기 뒤 추가
print(total)