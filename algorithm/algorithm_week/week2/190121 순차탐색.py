def sequentialSearch(a, n, key):   # a는 데이터, n은 데이터 길이, key는 찾으려는 값
    i = 0                          # i 변수 설정
    while i < n and a[i] != key:   # while문, i가 데이터 길이n보다 작을때, 그리고 a인덱스가 키와 같지 않을때까지 돈다
        i += 1                     # 즉, i 는 n이되거나, key 를 찾으면 중지!

    if i < n: return i
    else: return -1                  # 19는 data[5]에 위치...
data = [4, 9, 11, 23, 2, 19, 7]  # for문으로 구현해보기.
key = 19
print(sequentialSearch(data, len(data), key))