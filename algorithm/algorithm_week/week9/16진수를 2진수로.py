# import sys
# sys.stdin = open("16진수.txt")
#
# data = input()
# for i in data:
#     if i == '0':
#         print('0000', end = " ")
#     elif i == 'F':
#         print('1111', end=" ")
#
#################위 = 내방식 / 아래 = 강사님방식 #######################
def aToh(c):
    if c <= '9' : return ord(c)-ord('0')
    else: return ord(c)-ord("A") + 10

def makeT(x):
    for i in range(4):
        t.append(asc[x][i])
t = []
arr = "0F97A3"
asc = [[0,0,0,0],
     [0,0,0,1],
     [0,0,1,0],
     [0,0,1,1],
     [0,1,0,0],
     [0,1,0,1],
     [0,1,1,0],
     [0,1,1,1],
     [1,0,0,0],
     [1,0,0,1],
     [1,0,1,0],
     [1,0,1,1],
     [1,1,0,0],
     [1,1,0,1],
     [1,1,1,0],
     [1,1,1,1]]

for i in range(len(arr)):
    makeT(aToh(arr[i]))
n = 0
for i in range(len(t)):
    n = n * 2 + t[i]
    if i%7 == 6:
        print(n, end=", ")
        n = 0
if i % 7 !=6:
    print(n)



