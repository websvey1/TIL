INSERT INTO movies --다 추가할때는 컬럼명 일일히 추가할 필요 없음--
VALUES(20182530, '극한직업', '15세이상관람가', '이병헌', 20190123, 3138467, 111, '한국', '코미디');

SELECT * FROM movies
WHERE 영화코드=20040521;

DELETE FROM movies WHERE 영화코드=20040521;

SELECT * FROM movies
WHERE 영화코드=20185124;

UPDATE movies
SET 감독 = '없음'
WHERE 영화코드=20185124;

SELECT * FROM movies
WHERE 영화코드=20185124;