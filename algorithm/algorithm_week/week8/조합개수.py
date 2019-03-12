def comb(n,r,q):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return comb(n-1, r-1, q) + comb(n-1,r,q)

A = [1,2,3,4]
T = [0,0,0]
print(comb(4,3,3))