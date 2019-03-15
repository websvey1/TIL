data = int(input())
three = 0
five = data // 5
data = data % 5

while data !=0 and five >=0:
    if data %3 == 0:
        three = data //3
        data = data %3
        break

    five = five -1
    data +=5
print(data==0 and (three+five)or -1)
# if data ==0:
#     print(three+five)
# else:
#     print(-1)