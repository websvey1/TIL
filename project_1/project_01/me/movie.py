import requests
from bs4 import BeautifulSoup
import os
from pprint import pprint
import datetime
from datetime import timedelta
import csv
import json
token = os.getenv('token')

list_movie = []
with open('boxoffice.csv', newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_movie.append(row['m_cd'])
    # pprint(list_movie)
with open('movie.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ('Movie_code', 'Movie_name', 'Movie_nameEn', 'Movie_nameOg', 'prdt_year', 'Genres', 'Directors', 'Watch_grade', 'Actor1', 'Actor2', 'Actor3')
    writer = csv.DictWriter(f, fieldnames =fieldnames)
    writer.writeheader()
    for i in range(len(list_movie)):
        url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={token}&movieCd={list_movie[i]}'
        res = requests.get(url)
        movie_code = res.json()
        # pprint(movie_code)
        movie_codes = movie_code["movieInfoResult"]["movieInfo"]
        # pprint(movie_codes)
        if len(movie_codes["actors"]) == 0:
            writer.writerow({'Movie_code' : movie_codes["movieCd"], 'Movie_name' : movie_codes["movieNm"], 'Movie_nameEn' : movie_codes["movieNmEn"],
                        'Movie_nameOg' : movie_codes["movieNmOg"], 'prdt_year' : movie_codes["openDt"], 'Genres' : movie_codes["genres"][0]["genreNm"], 
                        'Directors' : movie_codes["directors"][0]["peopleNm"], 'Watch_grade' : movie_codes["audits"][0]["watchGradeNm"], 
                        'Actor1' : "", 'Actor2' : "", 'Actor3' : ""})
        elif len(movie_codes["actors"]) == 1:
            writer.writerow({'Movie_code' : movie_codes["movieCd"], 'Movie_name' : movie_codes["movieNm"], 'Movie_nameEn' : movie_codes["movieNmEn"],
                        'Movie_nameOg' : movie_codes["movieNmOg"], 'prdt_year' : movie_codes["openDt"], 'Genres' : movie_codes["genres"][0]["genreNm"], 
                        'Directors' : movie_codes["directors"][0]["peopleNm"], 'Watch_grade' : movie_codes["audits"][0]["watchGradeNm"], 
                        'Actor1' : movie_codes["actors"][0]["peopleNm"], 'Actor2' : "", 'Actor3' : ""})
        elif len(movie_codes["actors"]) == 2:
            writer.writerow({'Movie_code' : movie_codes["movieCd"], 'Movie_name' : movie_codes["movieNm"], 'Movie_nameEn' : movie_codes["movieNmEn"],
                        'Movie_nameOg' : movie_codes["movieNmOg"], 'prdt_year' : movie_codes["openDt"], 'Genres' : movie_codes["genres"][0]["genreNm"], 
                        'Directors' : movie_codes["directors"][0]["peopleNm"], 'Watch_grade' : movie_codes["audits"][0]["watchGradeNm"], 
                        'Actor1' : movie_codes["actors"][0]["peopleNm"], 'Actor2' : movie_codes["actors"][1]["peopleNm"], 'Actor3' : ""})
        else:
            writer.writerow({'Movie_code' : movie_codes["movieCd"], 'Movie_name' : movie_codes["movieNm"], 'Movie_nameEn' : movie_codes["movieNmEn"],
                        'Movie_nameOg' : movie_codes["movieNmOg"], 'prdt_year' : movie_codes["openDt"], 'Genres' : movie_codes["genres"][0]["genreNm"], 
                        'Directors' : movie_codes["directors"][0]["peopleNm"], 'Watch_grade' : movie_codes["audits"][0]["watchGradeNm"], 
                        'Actor1' : movie_codes["actors"][0]["peopleNm"], 'Actor2' : movie_codes["actors"][1]["peopleNm"], 'Actor3' : movie_codes["actors"][2]["peopleNm"]})
        
# with open('movie.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['Movie_code'], row['Movie_name'], row['Movie_nameEn'], row['Movie_nameOg'], row['prdt_year'], row['Genres'], row['Directors'], row['Watch_grade'], row['Actor1'], row['Actor2'], row['Actor3'])