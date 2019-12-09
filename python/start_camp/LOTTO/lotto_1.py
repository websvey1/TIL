from bs4 import BeautifulSoup
import requests
import random



numbers = random.sample(range(800, 838), 8)
for i in numbers:
    count = 0
    # when = requests.args.get('when')
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={i}"
    #req 텍스트화 .
    req = requests.get(url).text
    #soup 파싱
    soup = BeautifulSoup(req, "html.parser")

    week = soup.select(".ball_645")
    print(f"{i}회차 당첨번호")
    for result in week:
        print(result.text, end=" ")
        count += 1
        if count == 6:
            print("+", end = " ")
    print()
