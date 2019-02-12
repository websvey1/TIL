
# def push(item):
#     s.append(item)
#
# def pop():
#     if len(s) == 0:
#         print("stack is empty!")
#         return
#     else:
#         return s.pop(-1) # 여기 pop랑 def pop는 다름.
s = []
#    보완해야함...
def test(word):
    for i in word:
        if i == '(':
            s.append(i)
        elif i == ')' and '(' in s:
            s.pop()
        else:
            return False
    if len(s) != 0:
        return False
    else:
        return True

print(test('())'))


############ 강사님 / 다치지 못했음..

# def A(data):
#     for i in range(len(data)):
#         if data[i] == "(":
#             push(data[i])
#         elif data[i] == ")'":
#             if isEmpty():return False
#             pop()
#     if not isEmpty(): return False
#     else: return True

