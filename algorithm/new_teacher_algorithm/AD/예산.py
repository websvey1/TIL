import sys
sys.stdin = open('예산.txt')
#######################################################
########################강사님이진탐색 ####################
#######################################################
# def check(m):
#     tot = 0
#     for i in range(N):
#         if data[i] <=m: tot += data[i]
#         else: tot += m
#     if tot <= hap: return 1
#     else: return 0
# N = int(input())
# data = sorted(list(map(int, input().split())))
# hap = int(input())
# e = max(data)
# s = 1
# sol = 0
# while s<=e:
#     m = (s+e)//2
#     if check(m):
#         sol = m
#         s = m+1
#     else:
#         e = m-1
# print(sol)
#######################################################
########################그리디(강사님)########################
#######################################################
# N = int(input())
# data = sorted(list(map(int, input().split())))
# hap = int(input())
# cnt = 0
# result = 0
# for i in range(N):
#     if cnt+data[i]*(N-i) <= hap: # 현재 예산액으로 배정 가능하면,
#         cnt += data[i]
#     else:               #배정이 불가하다면
#         result = (hap-cnt)//(N-i)
#         break
# if result: print(result)
# else: print(data[N-1])
#######################################################
########################그리디(나 2차)########################
#######################################################
# N = int(input())
# data = sorted(list(map(int, input().split())))
# hap = int(input())
# cnt = 0
# result = 0
# for i in range(N):
#     if cnt+data[i]*(N-i) <= hap:
#         cnt += data[i]
#     else:
#         N = N-i
#         break
# result = (hap-cnt)//N # 2가 아니라 n이엇음
# print(result) 
                # 끝에 하나만 추가하면 됌

#######################################################
########################ㄴ 풀이 ########################
#######################################################
# N = int(input())
# data = sorted(list(map(int, input().split())))
# hap = int(input())
# avg = hap // N
# cnt_value = 0
# idx = []
# pas = 0
# for i in range(N):
#     if data[i] < avg:
#         N -=1
#         cnt_value += avg-data[i]
#     elif data[i] > avg:
#         idx.append(data[i])
#     else:
#         pas +=1
#     if pas == N:
#         print(cnt_value)
# avg += cnt_value //N
# idx.append(avg)
# print(min(idx))
