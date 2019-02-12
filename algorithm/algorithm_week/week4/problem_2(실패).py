import sys

sys.stdin = open("problem_2.txt", "r")
T = int(input())
# print(T)
for tc in range(1, T+1):
    data = input()
    result = 0
    goalho = []
    for i in data:
        if i == '(':
            goalho.append(i)
        elif i == '{':
            goalho.append(i)
        elif i == ')':
            goalho.append(i)
        elif i == '}':
            goalho.append(i)
    # print(goalho)
    for j in range(len(goalho)):
        if goalho[j] == '(':
            if ')' in goalho:
                del goalho[goalho.index(')')]
                del goalho[goalho.index('(')]
            # else:
            #     result = 0
            #     break
        elif goalho[j] == '[':
            if ']' in goalho :
                del goalho[goalho.index(']')]
                del goalho[goalho.index('[')]
            # else:
            #     result = 0
            #     break

        else:
            result = 0
        print(goalho)
    # if goalho == goalho[::-1] and len(goalho) % 2 == 0:
    #     result = 1
    # else:
    #     result = 0
    #
    # print(f'#{tc} {result}')
    