import sys
sys.stdin = open('괄호검사.txt')

T = int(input())
for tc in range(1,T+1):
    data = list(map(str, input()))
    # print(data)
    goalho = []
    for i in range(len(data)):
        if data[i] == '{' or  data[i] == '(':
            goalho.append(data[i])
        elif data[i] == '}' :
            if len(goalho) == 0:
                break
            else:
                # if goalho.pop() != '{':
                if goalho[-1] != '{':
                    break
                else:
                    goalho.pop()

        elif data[i] == ')':
            if len(goalho) == 0:
                break
            else:
                # if goalho.pop() != '(':
                if goalho[-1] != '(':
                    break
                else:
                    goalho.pop()
    if len(goalho) :
        # print(goalho)
        print('#%d' %(tc), 0)
    else:
        # print(goalho)
        print('#%d' %(tc), 1)