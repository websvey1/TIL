# 반복문
def cdgys(a,b):
    if a>b:
        I = b
    else:
        I = a
    while True:
        if a % I == 0 and b % I == 0:
            return I
        else:
            I = I //2

print(cdgys(8,18))