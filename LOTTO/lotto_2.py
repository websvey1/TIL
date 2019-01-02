import random
import requests
import json
from pprint import pprint

# 0. randome으로 로또번호 생성합니다.
# 1. api를 통해 우승번호를 가져옵니다.
# 2. 0번과 1번을 비교하여 나의 등수를 알려준다.

# URL요청해서 정보가져오기
#  -jason으로 받는다. (딕셔너리로 접근가능)
# API 당첨번호와 보너스번호를 저장하고
# 뽑은게 몇등인지 하는거 뽑으세요 





numbers = random.sample(range(1, 46), 6)
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
bonus = lotto["bnusNo"]
winner = []
lotto = res.json()
for i in range(1, 7):
    winner.append(lotto[f"drwtNo{i}"])

print("이번주 당첨번호:" + str(winner))
print("보너스번호:" + str(bonus))
count = 0
while True:
    count += 1
    my_numbers = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(my_numbers))
    if matched == 6:
        print("1st")
        print(count,"번만에 당첨되셨습니다.")
        break
    elif matched == 5:
        if bonus in my_numbers:
            print("2nd")
        else:
            # print("3rd")
            continue
    elif matched == 4:
        continue
        # print("4th")
    elif matched == 3:
        # print("5th")
        continue
        # print(count,"번만에 당첨되셨습니다.")
    else:
        # print("fuck")
        continue


# count = 0
# set_i = set(numbers)
# set_lucky = set(luck)
# # set_bonus = set(bonus)
# compare = len(set_i & set_lucky)
# # compare_b = len(set_i & set_bonus)
# # for i in compare ==6:
# if compare == 6:
#     print("축하합니다. 1등입니다. 당첨금은 3,144,449,125원 입니다.")
# # elif compare == 5:
# #     print("축하합니다. 2등입니다. 당첨금은 66,903,173원 입니다.")
# #     count += 1
# elif compare == 5:
#     print("축하합니다. 3등입니다. 당첨금은 1,562,848원 입니다")
#     count += 1
# elif compare == 4:
#     print("축하합니다. 4등입니다. 당첨금은 50,000원 입니다.")
#     count += 1
# elif compare == 3:
#     print("5등입니다. 당첨금은 5,000원 입니다.")
#     count += 1
# else:
#     print("로또하지마라")
#     count += 1
# print(compare)


###################################################################################            준석이코드             ######################################################################

# url ="https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
# res = requests.get(url)
# lotto = res.json()
# num = random.sample(range(1, 46), 6)
# number = set(num)
# lotto_number = []
# lo_num = []
# print(number)
# for i in range(1, 7):
#    lotto_number = lotto[f'drwtNo{i}']
#    if lotto_number != lo_num:
#        lo_num.append(lotto_number)
# count = 0
# set_lo_num = set(lo_num)
# while len(number & set_lo_num) != 6:
#    num = random.sample(range(1, 46), 6)
#    number = set(num)
#    if len(number & set_lo_num) == 6:
#        print("1등입니다.")
#        count += 1
#        break
#    elif len(number & set_lo_num) == 5:
#        set_lo_num1 = set_lo_num | {lotto['bnusNo']}
#        if len(number & set_lo_num1) == 6:
#         #    print("2등입니다.")
#             count += 1
#             continue
#        else:
#         #    print("3등입니다.")
#             count += 1
#             continue
#    elif len(number & set_lo_num) == 4:
#     #    print("4등입니다.")
#        count += 1
#        continue
#    elif len(number & set_lo_num) == 3:
#     #    print("5등입니다.")
#        count += 1
#        continue
#    else:
#        # print("꽝")
#        count += 1
#        continue
# print(count)
#######################################################################################################################   혜리코드
# import random
# import requests
# import json
# from pprint import pprint
# url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
# res = requests.get(url)
# lotto = res.json()
# win_num = []
# for i in range(1,7):
#     win_num.append(lotto[f"drwtNo{i}"])
# win_num = set(win_num)
# cnt = 0
# while True:
#     numbers = set(random.sample(range(1, 46), 6))
#     # print(numbers)
#     cnt += 1
#     luck = len(numbers - win_num)
#     if luck == 0:
#         print(f"축하합니다! 1등입니다.: {cnt}")
#         print(f"{1/cnt*100}%")
#         break
#     elif luck == 1:
#         if (numbers - win_num) == set({lotto["bnusNo"]}):
#             print(f"축하합니다! 2등입니다. 추첨 횟수 : {cnt}")
    #     else:
    #         print(f"축하합니다! 3등입니다. 추첨 횟수 : {cnt}")
    #         # break
    # elif luck == 2 :
    #     print(f"축하합니다! 4등입니다. 추첨 횟수 : {cnt}")
    #     # break
    # elif luck == 3 :
    #     print(f"축하합니다! 5등입니다. 추첨 횟수 : {cnt}")

