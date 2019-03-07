import sys
sys.stdin = open("덧셈.txt")

data = input().split()
comp=int(data[0])
mok, mod = 0, 0
hap = int(data[1])
nanum = 0
cnt =0
for i in range(1, 50):
    nanum = 10**i
    mok = comp//nanum
    mod= comp%nanum
    if mok+mod == hap:
        cnt += 1
        break
if cnt !=0:
    print('%d+%d=%d' %(mok, mod, hap))
else:
    print("NONE")

# ########혜리코드#############
# def plus(s, x):
#     for i in range(1, len(s)):
#         sa = int(s[:i])
#         sb = int(s[i:])
#         if sa+sb==x:
#             return str(sa)+'+'+str(sb)+'='+str(x)
#     return 'NONE'
# s, x = input().split()
# print(plus(s, int(x)))