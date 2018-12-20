# item = int(input("번호를 입력하세요: "))
# #자연수 N이 주어졌을 때, 1부터 N까지 한줄에 하나씩 출력하는 프로그램을 작성하시오

# for i in range(1, item)
#     print(i+1)

warn_investment_list = ['microsoft', 'google', 'naver', 'kakao', 'samsung', 'lg']
print(f"경고 종목 리스트 : {warn_investment_list}")
item = input('투자종목이 무엇입니까?: ')

if item in warn_investment_list:
    print("투자경고종목입니다")
else:
    print("투자 경고 종목이 아닙니다.")