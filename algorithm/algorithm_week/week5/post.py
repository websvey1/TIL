# 후위 표기
def post(word):
    stack = []
    munja = []
    munja.extend(word)
    # print(munja)
    for i in range(len(munja)):
        if munja[i] == "+" or munja[i] == "-"or munja[i] == "*" or munja[i] == "/":
            stack.append(munja[i])
        else:
            print(munja[i], end="")
    while len(stack) != 0:
        print(stack.pop(), end="")




post("2+3*4/5")



