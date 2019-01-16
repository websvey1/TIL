# for i in range(2,10):
#     for j in range(1,10):
#         a = i * j
#         print(a)
def bubbleSort(data):
    for i in range(len(data)-1, 0, -1): # 4 3 2 1
        for j in range(0, i):  # 4 3 2 1 번
            if data[j] < data[i]:
                data[j], data[j+1] = data[j+1], data[j]


data = [55, 78, 7, 12, 42]
bubbleSort(data)
print(data)