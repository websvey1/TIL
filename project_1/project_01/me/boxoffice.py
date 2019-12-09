import requests
from bs4 import BeautifulSoup
import os
from pprint import pprint
import datetime
from datetime import timedelta
import csv
import json

token = os.getenv("token")
today = datetime.datetime(2019, 1, 20)
day_minus_count = timedelta(days=-7)

with open('boxoffice.csv', 'w', newline='', encoding='utf-8') as f:
    type_name = ('m_cd', 'm_title', 'm_aud', 'm_rec')
    writer = csv.DictWriter(f, fieldnames=type_name)
    writer.writeheader()
    overlap = []
    for i in range(10):
        today += day_minus_count
        count_day = today.strftime('%Y%m%d')
        for j in range(10):
            url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={token}&targetDt={count_day}&weekGb='
            res = requests.get(url)
            m_list = res.json()
            m_list_a = m_list["boxOfficeResult"]["weeklyBoxOfficeList"]
            if m_list_a[j]["movieNm"] not in overlap:
                overlap.append(m_list_a[j]["movieNm"])
                writer.writerow({'m_cd':m_list_a[j]["movieCd"], 'm_title' : m_list_a[j]["movieNm"], 'm_aud' : m_list_a[j]["audiAcc"], 'm_rec' : count_day})
