# 지니뮤직 크롤링, 원하는 날짜로
# 원하는 날짜를 입력 > 입력된 날의 인기차트 크롤링

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

input_date = input('원하는 날짜를 입력해 주세요 (예. 20200713): ')

response = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd='+input_date.strip(),
    headers=headers
)

# HTML 데이터 가공
soup = BeautifulSoup(response.text, 'html.parser')

# 순위 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# 곡 제목 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# 가수 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.artist.ellipsis

selector = '#body-content > div.newest-list > div > table > tbody > tr'
num_selector = 'td.number'
title_selector = 'td.info > a.title.ellipsis'
artist_selector = 'td.info > a.artist.ellipsis'

num = soup.select(selector)
title = soup.select(selector)
artist = soup.select(selector)

for list_num in num:
    num_tag = list_num.select_one(num_selector)
    title_tag = list_num.select_one(title_selector)
    artist_tag = list_num.select_one(artist_selector)

    if num_tag:
        # print(num_tag.text, title_tag.text, artist_tag.text)

        num_return = num_tag.text[0:5].strip()
        title_return = title_tag.text.strip()
        artist_return = '['+artist_tag.text.strip()+']'

        print(num_return, title_return, artist_return)

