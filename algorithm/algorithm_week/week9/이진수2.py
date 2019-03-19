import sys
sys.stdin = open("이진수2.txt")
T = int(input())
for tc in range(1,T+1):
    data = float(input())
    real = ''
    while len(real) < 14:
        data = data * 2
        if data > 1:
            data -=1
            real += '1'
        elif data < 1:
            real += '0'
        elif data == 1:
            real += '1'
            break

    if len(real) >= 13:
        print('#%d' %(tc), "overflow")
    else:
        print('#%d' %(tc), real)