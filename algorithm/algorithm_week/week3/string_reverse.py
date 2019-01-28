# A = 'algorithm'   # 알고리즘 문자열 순서 바꾸기
# a = ''
# for i in range(len(A)):
#     # a.append(A[9-(i+1)]) # 이건 각각 개별 분리되서 join으로 묶어야함
#     a += A[9-(i+1)]
# print(a)

# # 강사님코드
# def my_str(ary):
#     str = list(ary)
#     for i in range(len(str)//2):
#         t = ary[i]
#         str[i] = str[len(str)-1-i]
#         str[len(ary)-1-i] = t
#     ary = "".join(str)
#     return ary
# print(my_str('1234567'))

# #강사님 코드 2
# a = '1234567'
# a = a[::-1]
# print(a)

# 비교하기
# def strcmp(str1, str2):
#     i = 0
#     if len(str1) != len(str2):
#         return False
#     else:
#         while i < len(str1) and i < len(str2):
#             if str1[i] != str2[i]:
#                 return False
#             i += 1
#         return True
    
# print(strcmp('aasdf', 'asdf'))

# # aoi함수 구현
# def atoi(string):
#     value = 0
#     i = 0
#     while (i < len(string)):
#         c = string[i]
#         if c>= '0' and c <='9':
#             digit = ord(c) - ord('0')
#         else:
#             break
#         value = (value*10) + digit
#         i += 1
#     return value
# print(atoi('123123123aa'))

# # 이건 왜하는거지?  == 문자열 교체하기 ! abc 1,2 ABC의 내용 중 1,2를 one twoㄹ 바꾸는것
# str1 = "abc 1, 2 ABC"
# str1 = str1.replace("1, 2", "one, Two")
# print(str1)

# # 양의 정수르 ㄹ받아 문자열로 변환하기
# def itoa(x):
#      str = list()
#      y = 0
#      while True:
#          y = x % 10
#          str.append(chr(y + ord('0')))
#          x //= 10
#          if x == 0 : break
#      str.reverse()
#      str = "".join(str)
#      return str
# x = 123
# str1 = itoa(x)
# print(str1, type(str1))

# 고지식한 알고리즘
# p = "bird"
# t = "The early bird catches the worm"
# M = len(p)
# N = len(t)
#
# def BruteForce(p, t):
#     i = 0
#     j = 0
#     while j < M and i < N:
#         if t[i] != p[j]:
#             i = i-j
#             j = -1
#         i = i + 1
#         j = j + 1
#     if j == M:
#         return i-M
#     else:
#         return -1
# print(BruteForce(p, t))#
# #상근이형
# def brute_force(array, key):
#    for i in range(len(array)-len(key)+1):
#        j = i
#        for k in key:
#            if k != array[j]:
#                break
#            else:
#                j += 1
#        else:
#            return i
#
#    return False
#
# array = "abcdefghjikejejrkewrhjkewhrkhejkr"
# key = 'jk'
# print(brute_force(array,key))

# bit별 암호화

def bit(a):
    for i in range(7, -1, -1):
        if a & (1<<i):
            print(1, end="")
        else:
            print(0, end="")
    print()
a = 0x86
key= 0xAA
print("a        ==>", end="")
bit(a)

print("a^=key ==>", end="")
a ^= key
bit(a)

print("a^=key ==>", end="")
a ^= key
bit(a)