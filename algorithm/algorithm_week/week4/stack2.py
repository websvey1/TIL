#  C style
SIZE = 100
stack = [0] * 100
top = -1

def push(item):
    global top
    if top > SIZE -1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("stack is empty!")
        return 0
    else:
        result = stack[top]
        top -= 1
        return result

# python style
# def push(item):
#     s.append(item)

# python style
# def pop():
#     if len(s) == 0:
#         print("stack is empty!")
#         return
#     else:
#         return s.pop(-1) # 여기 pop랑 def pop는 다름.
# s = []



push(5)
push(2)
push(1)
# push(5,1,2,3) # 뭉텅이로 들어가면 튜플로 묶여서 ㄷㄹ어감
# print(pop())  # 나올때도 뭉텅이로 나옴
print(pop())     #여기 pop랑 python method pop랑 다른거같다.
print(pop())
print(pop())
print(top, stack)