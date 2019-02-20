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
                stack.append(int(stack.pop(-2))//int(stack.pop(-1)))   # 나누기는 자연수
            else:
                stack = ["error"]
                break

        elif data[i] == ".":
            if len(stack) == 1:                  # 여기 25~30을 and로 묶으려 하다보니오류가 떴음.
                break
            else:
                stack = ["error"]
                break
        else:
            stack.append(data[i])

    print(f'#{tc} {stack[0]}')


    # print(data)