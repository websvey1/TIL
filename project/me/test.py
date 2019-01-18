lunch = {
  '용성돌솥비빔밥':'054-474-7119',
  '별난짬뽕':'054-473-3040',
  '매콤돈가스':'054-472-2030'
}

# 1. string formatting
with open('lunch.csv','w') as f:
    for item in lunch.items():
        print(f.write(f'{item[0]},{item[1]}\r\n'))
    

# 2. join
with open('lunch.csv','w') as f:
    for item in lunch.items():
        print(f.write(','.join(item)+'\r\n'))

# 3. csv.writer
import csv
with open('lunch.csv','w') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)


# 4. csv.DictWriter
import csv
with open('names.csv', 'w', newline='') as f:
    fieldnames = ('first_name', 'last_name')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

import csv
import requests
import json
import os
import datetime
from datetime import timedelta
from bs4 import BeautifulSoup

days = datetime.datetime(2019, 1, 20)
ago = timedelta(days=-7)
with open('names.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('movie_code', 'title', 'audience', 'recorded_at')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for k in range(10):
        days = days + ago
        days_ago = days
        days_ago = days_ago.strftime('%Y%m%d')
        for i in range(10):
            url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt={days_ago}&weekGb=0"
            res = requests.get(url)
            movie_list = res.json()
            movie_lists = movie_list["boxOfficeResult"]["weeklyBoxOfficeList"]
            writer.writerow({'movie_code' : movie_lists[i]["movieCd"], 'title' : movie_lists[i]["movieNm"], 'audience' : movie_lists[i]["audiAcc"],'recorded_at' : days_ago})
            print(f'실행중{i}')
        
with open('names.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['movie_code'], row['title'], row['audience'], row['recorded_at'])









        