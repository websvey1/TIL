data = 105

a = 300
b = 60
c = 10
cnt_a = 0
cnt_b = 0
cnt_c = 0
while c <= data:
    if data >= a:
        data -= a
        cnt_a += 1
        continue
    elif data >= b:
        data -= b
        cnt_b += 1
        continue
    elif data >= c:
        data -= c
        cnt_c += 1
        continue

if data == 0:
    print(f'{cnt_a} {cnt_b} {cnt_c}')
else:
    print(-1)