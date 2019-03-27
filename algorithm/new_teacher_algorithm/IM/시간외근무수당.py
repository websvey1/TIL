import sys
sys.stdin = open("시간외근무수당.txt")
hap = 0
for tc in range(5):
    a = input().split()
    if float(a[1])-float(a[0])>1.0:
        if float(a[1])-float(a[0])-1 <= 4.0:
            hap += float(a[1])-float(a[0])-1
        else:
            hap += 4


if hap >= 15:
    print(int(hap*0.95*10000))
elif hap <= 5:
    print(int(hap*1.05*10000))
else:
    print(int(hap*10000))