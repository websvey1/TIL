# sort_test = [4, 1, 5, 7, 9] # 테스트 리스트 생성
# print(sorted(sort_test)) # sorted 정렬 성공
# print(sort_test) # 기존 sort 변경 여부 확인
# sort_test_sort = sort_test.sort() #sort 정렬 테스트
# print(sort_test_sort) # None
# print(sort_test)




# OOP test
# class Person():
#     def __init__(self, name, age):
#         self.name = name
# p1 = Person(p1, 'hong', 100)  # p1이없음...
# p2 = Person('kim') # 필수요서인 age가 없음
# p3 = Person(age = 3, name = 'kang')
# p4 = Person() # 둘다 없음.

# l e g b  순서
# L Local: 함수 내 정의된 지역 변구
# E Enclosing Function Local: 함수를 내포하는 또다른 함수 영역
# 파이썬은 다른 언어와 다르게 함수 내부에 또 다른 함수를 정의 할 수 있다.(내포된 함수)
# G Global: 함수 영역에 포함되지 않는 모듈 영역
# B Built-in: 내장 영역
# a = 1
# def m_1():
#     a = 5
#     m_2()
# def m_2():
#     print(a, end='')
# m_1()
# print(a)

#  OOP greeting # 여기서 choi가 나오게 하려면>
# name = 'hong'
# class Person:
#     name = 'choi'

#     def greeting(self):
#         print(name)
# p1 = Person()
# p1.name = 'kim'
# p1.greeting()

# def func(a, b=1, c=2, *args, **kwargs):
#     d = sum([n*2 for n in args if n>=2])
#     e = sum([v*v for k,v in kwargs.items()])
#     return a+ b+ c+ d+e

# print(func(9, 4, 2, 3, 1, 7, d=3, e=6))

# 리스트 컴프레히션 테스트
# for i in range(5):
#     if i > 2:
#         print(i)
# [print(i) for i in range(5) if i>2]

# args 받기
# def func(c = '5', *args):
#     c = '3'
#     a,c,b = args
#     return a+b+c
# print(func('3', '4', '1', '2'))

#upper
# string = "i1m hungry"
# result = ""
# for idx, val in enumerate(string):
#     if idx % 2:
#         result += val.upper()
#     else:
#         result += val
# print(result)

# dict_a = {'apple':1, 'banana':2, 'lemon':3}
# list_b = ['1','2','3']
# list_c = [5,6,7]
# print(dict_a['apple'])
# print(dict_a.get('lemon'))
# print(map(int, list_b))
# B = list_c.pop()
# print(B)

# a = {'cherry':1, 'apple':2, 'melon':5}
# # print(''.join(a))
# print(a.get('apple'))

# a = [i if i%2 else i+1 for i in range(10)]
# import math
# print(dir(math))

# str_a = '1234'
# print(str_a[::-1])

# a = 0 and 5 and 7
# b = 0 or 2 and 3
# c = 3 or 2 or 1
# print(a,b,c)

# a = [1,2,3,4,5]
# print(a.pop(2))

# name = 'A'
# class Person:
#     name = 'B'
#     def __init__(self):
#         self.name = name
#     def introduce(self):
#         return self.name
# h2 = Person()
# print(h2.introduce)

a = {'inner':{}}
print(len(a))
a['inner']['key']=1
print(a)