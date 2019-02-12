import sys

sys.stdin = open("problem_2.txt", "r")

def test(word):
    s = []
    for i in word:
        if i == '(':
            s += i
        elif i == '{':
            s += i
        elif i == ')':
            if '(' not in s:
                return 0
            else:
                s.pop()
        elif i == '}':
            if '{' not in s:
                return 0
            else:
                s.pop()
        elif i == ')':
            s.pop()
        elif i == '}':
            s.pop()
    if len(s) != 0:
        return 0
    else:
        return 1

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
    word = ''.join(goalho)
    # print(word)

    print(f'#{tc} {test(word)}')
