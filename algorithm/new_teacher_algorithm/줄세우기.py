import sys
sys.stdin = open("줄세우기.txt")
T = int(input())
# people = [i for i in range(1,T+1)]
# print(people)
result = []
data = list(map(int, input().split()))
# print(data)
for i in range(1,T+1):
    result.insert(len(result)-data[i-1], i)
for i in result:
    print(i, end=" ")