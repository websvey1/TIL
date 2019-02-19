import sys
sys.stdin = open("problem_1.txt")

T = int(input())

for tc in range(1, T+1):
    stack = []
    result= []
    buho = ["+","-","*","/"]
    data = list(input().split())
    for i in range(len(data)):
        if data[i] in buho:
            if data[i] == "+" and len(stack)>1:
                stack.append(int(stack.pop(-2))+int(stack.pop(-1)))

            elif data[i] == "-" and len(stack)>1:
                stack.append(int(stack.pop(-2))-int(stack.pop(-1)))

            elif data[i] == "*" and len(stack)>1:
                stack.append(int(stack.pop(-2))*int(stack.pop(-1)))

            elif data[i] == "/" and len(stack)>1:
                stack.append(int(stack.pop(-2))/int(stack.pop(-1)))
            else:
                stack = ["error"]


        elif data[i] == ".":
            # print(stack)
            break
        else:
            stack.append(data[i])

    print(f'#{tc} {stack[0]}')


    # print(data)