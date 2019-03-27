import sys
sys.stdin = open("나는학급회장.txt")

N = int(input())
data = [list(map(int, input().split())) for i in range(N)]
re_data = [[0 for _ in range(N)] for _ in range(3)]
MMAAXX = 0
MAX_INDEX = 0
COMP_INDEX = 0
for i in range(N):
    for j in range(3):
        re_data[j][i] = data[i][j]
for k in range(len(re_data)):
    if sum(re_data[k]) > MMAAXX:
        MMAAXX = sum(re_data[k])
        MAX_INDEX = re_data.index(re_data[k])
    if sum(re_data[k]) == MMAAXX:
        COMP_INDEX = re_data[k].index(re_data[k])
        if re_data[MAX_INDEX].count(3) <re_data[COMP_INDEX].count(3):
            MAX_INDEX = COMP_INDEX
        elif 


print(MMAAXX)
print(MAX_INDEX)