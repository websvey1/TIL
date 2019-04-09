# def con(x,n,k):
#     if x==3:
#         cnt = 0
#         for i in range(len(test)):
#             if test[i] ==1:
#                 cnt +=1
#         if cnt==3:
#             a.append(test[:])
#             print(test)
#         return
#     else:
#         for i in range(x,n):
#             if test[i]:continue
#             test[i] = 1
#             con(x+1,n,k)
#             test[i] = 0
# def con(x,n,cnt):
#     if cnt==3:
#         print(test)
#         return
#     if x>=n:
#         return
#     else:
#         test[x] = 1
#         con(x + 1, n, cnt+1)
#         test[x] = 0
#         con(x+1,n,cnt)


a = []
test = [0,0,0,0,0,0,0,0]
con(0,len(test),0)
print(a)