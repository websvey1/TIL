import sys
sys.stdin = open("workshop.txt.txt", "r")
for tc in range(1, 11):
    V, E = map(int, input().split())
    data = {}
    visit = [0 for _ in range(V+1)]
    a = list(map(int, input().split()))
    for i in range(0, len(a), 2):
        if a[i] not in data.keys():
            data[a[i]] = [a[i + 1]]
        else:
            data[a[i]] += [a[i + 1]]
    print(data)
# print(visit)