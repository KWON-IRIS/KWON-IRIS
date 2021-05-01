import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

response = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',
    headers=headers
)

# print(response.text)

# HTML 데이터 가공

soup = BeautifulSoup(
    response.text, 'html.parser')

# 크롬 내 copy selector 사용.
# old_content > table > tbody > tr:nth-child(3) > td.title > div > a
# old_content > table > tbody > tr:nth-child(2) > td.point

selector = '#old_content > table > tbody > tr'
title_selector = 'td.title > div > a'
star_selector = 'td.point'
titles = soup.select(selector)
star = soup.select(selector)


count = 0

for title in titles:
    title_tag = title.select_one(title_selector)
    star_tag = title. select_one(star_selector)
    count = count + 1
    if title_tag:

        print(format(count, '02'), title_tag.text, star_tag.text)
