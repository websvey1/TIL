# arr = [[0, 1, 2, 3],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11]]
#
# for i in range(len(arr)):             # len(arr)은 [0,1,2,3], [4,5,6,7], [8,9,10,11] 으로 3이다
#     for j in range(len(arr[i])):      # len(arr[i])는  4이다 , [0,1,2,3] [4,5,6,7], [8,9,10,11] 모두 4개의 원소를 갖기때문
#         print(arr[i][j], end= " ")
#     print()
# print()
# print(len(arr))
#
# for j in range(len(arr[0])):
#     for i in range(len(arr)):
#         print(arr[i][j], end= " ")
#     print()
# print()

#############################################################연습문제#########################################

# import random
# a = [[1,1,1,1,1],
#      [1,0,0,0,1],
#      [1,0,0,0,1],
#      [1,0,0,0,1],
#      [1,1,1,1,1]]
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# def isWall(x,y):
#     if x < 0 or x >= 5: return True
#     if y < 0 or y >= 5: return True
#     return False
# def calAbs(y,x):
#     if y - x > 0: return y - x
#     else: return x - y
# sum = 0
# for x in range(len(a)):
#     for y in range(len(a[x])):
#         for i in range(4):
#             testX = x + dx[i]
#             testY = y + dy[i]
#             if isWall(testX, testY) == False:
#                 sum += calAbs(a[y][x], a[testY][testX])
# print("sum = {}".format(sum))


