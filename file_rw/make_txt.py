# #파일생성
# f = open("new.txt", "w")
# f.write("Hello !!!")
# f.close()

# with open("new.txt", "w") as f:
#     f.write("Hello !!!")
# 위와 아래와 완전히 동일한 코드임
# "Hello !!!와 다른 내요을 쓰면 내용이 바뀜."


###읽고쓰기###
# f = open("new.txt", "r")
# data = f.read()
# print(data)
# f.close() => 단순히 bssh에 나오게 함.

# with open("new.txt", "r") as f:
#     data = f.read()
#     print(data)

# f = open("new.txt", "w", encoding='utf-8')
# for i in range(1, 10):
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
# f.close()

# with open("new.txt", "w", encoding = 'utf-8') as f:
#     for i in range(1, 10):
#         data = f'{i}번째 줄입니다.\n'
#         f.write(data)

# menu = ["카레\n", "짜장\n", "탕수\n"]
# f = open("menu.txt", "w", encoding = 'utf-8')
# f.writelines(menu)
# f.close()


################################################################################
##절대 보지 말고 할것##
f = open("multi.txt", "w", encoding = "utf-8") 
for i in range(1, 6):
    data = f'{i}번 째 줄입니다.\t'
    f.write(data)