import sys
sys.stdin = open("이진수.txt")

T = int(input())
for tc in range(1, T+1):
    N,data = input().split()
    N = int(N)
    table = ['0000',  #0
             '0001',  #1
             '0010',  #2
             '0011',  #3
             '0100',  #4
             '0101',  #5
             '0110',  #6
             '0111',  #7
             '1000',  #8
             '1001',  #9
             '1010',  #A
             '1011',  #B
             '1100',  #C
             '1101',  #D
             '1110',  #E
             '1111']  #F
    print('#%d' % (tc), end=" ")
    for i in range(N):

        if data[i] == '0':
            print(table[0], end="")
        elif data[i] == '1':
            print(table[1], end="")
        elif data[i] == '2':
            print(table[2], end="")
        elif data[i] == '3':
            print(table[3], end="")
        elif data[i] == '4':
            print(table[4], end="")
        elif data[i] == '5':
            print(table[5], end="")
        elif data[i] == '6':
            print(table[6], end="")
        elif data[i] == '7':
            print(table[7], end="")
        elif data[i] == '8':
            print(table[8], end="")
        elif data[i] == '9':
            print(table[9], end="")
        elif data[i] == 'A':
            print(table[10], end="")
        elif data[i] == 'B':
            print(table[11], end="")
        elif data[i] == 'C':
            print(table[12], end="")
        elif data[i] == 'D':
            print(table[13], end="")
        elif data[i] == 'E':
            print(table[14], end="")
        elif data[i] == 'F':
            print(table[15], end="")
    print()
