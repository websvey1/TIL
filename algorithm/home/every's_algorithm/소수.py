# n = 5
# a = []
# for i in range(1,n+1):
#     if n % i == 0:
#         a.append(i)
#         print(f'{i}(은)는 {N}의 약수입니다.')
# if len(a)==2:
#     print(f'{N}(은)는 {a[0]}과 {a[1]}로만 나눌 수 있는 소수입니다.')

# a = []
# for i in range(1,201):
#     if i == 7:
#         print(i)
#     elif i%7==0 and i%5 !=0:
#         print(i)
a = []
b = 0
for i in range(100,301):
    if i %2 == 0:
        b = "".join(str(i))
        # print(b)
# for j in range(len(a)):
        if int(b[0]) % 2 == 0 and int(b[1]) % 2 == 0 and int(b[2]) % 2 == 0:
            a.append(b)
# print(a)
for j in range(len(a)):
    if j != len(a)-1:
        print(a[j], end=",")
    else:
        print(a[j])