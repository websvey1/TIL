#number = [2, 3, 6, 11, 8]
#for i in number:
#    print (i, end=" ")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
even = []
for numbers in number:
    if numbers % 2 == 0:
        even.append(numbers)
    else :
        odd.append(numbers)
print(odd,"홀수입니다")
print(even, "짝수입니다")