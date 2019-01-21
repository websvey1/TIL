def binarySerch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
        middle = (start +end) // 2
        if key == a[middle]:
            return middle
        elif key < a[middle]:
            end = a[middle] -1
        else:
            start = a[middle] +1
    return -1

key = 22
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySerch(data, key))