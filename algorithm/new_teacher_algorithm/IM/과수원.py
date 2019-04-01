import sys
sys.stdin = open('과수원.txt')

N = int(input())
data = [list(map(int, input())) for _ in range(N)]
# print(data)
point = []
cnt = 0
for i in range(N-1):
    for j in range(N-1):
        point.append((i,j))

for i in range(len(point)):
    a,b = point[i]
    sep_hap = [0] *4
    # print(sep_hap)
    for r in range(N):
        for c in range(N):
            if r<=a and c <=b:   # 내가 a랑 r 위치 / c와 b위치를 바꾸었었음
                sep_hap[0] += data[r][c]
            if r>a and c <=b:
                sep_hap[1] += data[r][c]
            if r<= a and c > b:
                sep_hap[2] += data[r][c]
            if r>a and c > b:
                sep_hap[3] += data[r][c]
    # print(point[i])
    # print(sep_hap)
    # if sep_hap == [1,1,1,1]:
    #     cnt +=1

    if sep_hap[0] == sep_hap[1] and sep_hap[0] == sep_hap[1] and sep_hap[1] == sep_hap[2] and sep_hap[2] == sep_hap[3]:
        cnt +=1
    elif cnt ==0:
        cnt = -1
print(cnt)