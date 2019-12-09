#파이썬 딕셔너리 활용 기초!

# dict = {
#     "대전": 23,
#     "서울": 30,
#     "구미": 20
# }

# print(type(dict.values()))

# list = [1, 2, 3]
# print(len(list))
######평균구하기######
# score = {
#     "국어": 87,
#     "영어": 92,
#     "수학": 40
# }
# aver = sum(score.values())
# print(aver/3)

# hap = 0
# for i in score:
#     hap += score[i]
# print(hap/len(score))

####################################################################################################################3
#반평균을 구하시오
# scores = {
#     "철수": {
#         "수학": 80,
#         "국어": 90,
#         "음악": 100
#     },
#     "영희": {
#         "수학": 70,
#         "국어": 60,
#         "음악": 50
#         }
#     }
##내꺼
# total_scores = scores.values()
# print(total_scores)
# # chap = 0
# # yhap = 0
# for i in total_scores:
#     for  in total_scores.

####강사님
# total_scores = 0
# count = 0
# for person_scores in scores.values():
#     for indivisual_scores in person_scores.values():
#         total_scores += indivisual_scores
#         count += 1
# average_score = total_scores / count
# print(average_score)

# total_score = 0
# total_score1 = 0
###############준석
# for i in scores.values():
#    for j in i.values():
#        total_score1 += j / len(i)
#    total_score += total_score1
#    total_score1 = 0
#    print(total_score)

# averge_score = total_score / len(scores)
# print(averge_score)


#3번  도시 중에 최근 3일 중 가장 추웠던곳, 가장 더웠던곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}
hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0
for name, temp in cities.items():
    #  name = 서울
    #  temp = [-6 -10 5] << 기준점
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        #최저 온도가 clod보다 더 추우면 cold에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
            #최고온도가 hot보다 ㄴㅍ으면 hot에넣기
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1
print(f"{hot_city}, {cold_city}")
    for i in max(tmp):
        if i > tmp:
            i = tmp
        else:
            continue

    
    for i in tmp:

    if tmp :
        print(name, tmp)
    else:
        pass
    print(name, max(tmp))

scores = {
    "국어": 87,
    "영어": 92,
    "수학": 40
}
for key, value in scores.items():
    print(key)
    print(value)

