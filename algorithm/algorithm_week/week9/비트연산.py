# def Bbit_print(i):
#     output = ""
#     for j in range( 7, -1, -1):
#         output += "1" if i & (1 << j) else "0"
#     print(output)
#
# for i in range(-5, 6):
#     print("%3d = " % i, end="")
#     Bbit_print(i)




########### 2진수로 입력받기 #####################
# data = int(input(), 2)
# print(data)

##############################################

arr = [0,0,0,0,0,0,0,1,1,1,   1,0,0,0,0,0,0,1,1,0,   0,0,0,0,0,1,1,1,1,0,   0,1,1,0,0,0,0,1,1,0,   0,0,0,1,1,1,1,0,0,1,   1,1,1,0,0,1,1,1,1,1,   1,0,0,1,1,0,0,1,1,1]
for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        n = n*2 + arr[j]
    print(n, end=" ")
print()