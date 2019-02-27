N = 4
# N = int(input())
data = [[4,'N'], [7,'Y'], [5,'N'], [6,'Y']]
# data = [input().split() for t in range(N)]

compmin = []
comp = []
for i in range(len(data)):
    if data[i][1] == 'Y':
        comp.append(int(data[i][0]))
    elif data[i][1] == 'N':
        compmin.append(int(data[i][0]))

if comp == []:
    print("F")
elif max(compmin) < min(comp):
    print(min(comp))
elif max(compmin) >= min(comp):
    print("F")
