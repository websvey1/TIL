def calc(equation):
    copy = equation
    symbol = []               ###기호리스트
    digit = []                ### 숫자리스트
    for i in copy:                           ###숫자만 스플릿
        if i.isdigit() == False:
        symbol.append(i)
        copy = copy.replace(i, " ")

    digit = list(map(int,copy.split()))
    if len(digit) == len(symbol):            ### 맨앞에 기호일 경우 첫 값 수정
        if symbol[0]=='-':
            digit[0] = -digit[0]
            del symbol[0]
        else:
            del symbol[0]

    while len(symbol)>0:                    ### 기호 1개 당 숫자 2개 계산
        if symbol[0] == '+':
            digit[0]=digit[0]+digit[1]
            del digit[1]
            del symbol[0]
        else:
            digit[0]=digit[0]-digit[1]
            del digit[1]
            del symbol[0]
            #print(digit)

    return digit[0]                       ### 반환
    return digit[0]                       ### 반환