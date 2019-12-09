

import requests
from bs4 import BeautifulSoup
# import bs4.beautifulsoup

# req = requests.get("https://www.nate.com/").text
# soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one("#divContentsUpper" )

# print(kospi.text)
############################

# req = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8B%A4%EC%8B%9C%EA%B0%84+%EA%B2%80%EC%83%89%EC%96%B4&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+%EA%B2%80%EC%83%89%EC%96%B4&tqi=UtASKlpySDGssu9aKAZssssssp0-188579").text
# soup = BeautifulSoup(req, 'html.parser', from_encoding='utf-8')
# kospi = soup.select_one("#nxfr_htp > div.realtime_srch._aside_news_tab" )

# print(kospi.text)

req = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(req, 'html.parser')
# kospi = soup.select_one(".PM_CL_realtimeKeyword_rolling .ah_item" )

# for tag in soup.select(".PM_CL_realtimeKeyword_rolling .ah_item"):
#     rank = tag.select_one('.ah_r').text
#     name = tag.select_one('.ah_k').text
#     print(f'{rank}는  {name}입니다.')

# for i in kospi:
#     name = i.select_one("ah_k")
#     print(name)

##############################
#강사님 코드

joo = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul")
joorang = joo.select_one(".ah_r").text


print(joorang)