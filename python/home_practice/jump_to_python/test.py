# def palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False
# print(palindrome('asdasa'))

# 양의 정수 x를 입력받아 제곱근의 근사값의 결과 반환

# def ROOT(num):
#     a = 0
#     b = num*2
#     for i in range(10):
#         c = (a+b)/2
#         if c**2 > num:
#             b = c
#         else:
#             a = c
#     return (a+b)/2
# print(ROOT(15))
#
# class Person():
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#     def greeting(self):
#         print(f'안녕하세요{self.name}. {self.age}살입니다')
# p1 = Person('홍길동', 20)
# p1.greeting()
# p2 = Person('둘리')
# p2.greeting()

class Circle():
    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def center(self, a=0, b=0):
        return (a,b)

    def move(self, a, b):
        self.a = a
        self.b = b
        return (a, b)

c1 = Circle(3)
print(c1.center())
print(c1.move())

