def hanoi(n, S, E, M):
    if n == 1:
        print(S, "->", E)
        return
    hanoi(n-1, S, M, E)

    # print(S, "->", E)

    hanoi(n-1, M, E, S)
# print("n=1")

hanoi(1, 1, 3, 2)

# print("n=2")
hanoi(2,1,3,2)

# print("n=3")
hanoi(3,1,3,2)

