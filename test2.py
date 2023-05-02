import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 검색어와 검색 기간 설정
query = '테슬라'
start_date = datetime.now() - timedelta(weeks=1)
end_date = datetime.now()

# 검색 기간 URL 생성
start_date_str = start_date.strftime('%Y.%m.%d')
end_date_str = end_date.strftime('%Y.%m.%d')
url_template = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds={start_date_str}&de={end_date_str}&docid=&nso=so%3Add%2Cp%3Afrom{start_date_str.replace(".", "")}to{end_date_str.replace(".", "")}%2Ca%3Aall&mynews=0&refresh_start=0&related=0'

# 첫 페이지에서 마지막 페이지 번호 추출
url = url_template.format(query=query, start_date_str=start_date_str, end_date_str=end_date_str, start=1)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
last_page = int(soup.select('.paging .btn_last')[0]['href'].split('start=')[-1])

# 각 페이지에서 기사 제목과 링크 가져오기
articles = []
for page in range(1, last_page + 1):
    url = url_template.format(query=query, start_date_str=start_date_str, end_date_str=end_date_str, start=(page - 1) * 10 + 1)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.select('.list_news .news_wrap .news_area'):
        title = item.select_one('.news_tit').text
        link = item.select_one('.news_tit')['href']
        articles.append({'title': title, 'link': link})

# 결과 출력
for article in articles:
    print(article['title'])
    print(article['link'])
    print('-' * 50)
