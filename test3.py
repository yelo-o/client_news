


import requests
from bs4 import BeautifulSoup

# 스크래핑할 첫 페이지 url
url_template = 'https://search.naver.com/search.naver?where=news&query=파이썬&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds=2023.04.26&de=2023.05.03&docid=&nso=so%3Add%2Cp%3Afrom20230426to20230503%2Ca%3Aall&mynews=0&refresh_start=0&related=0'

# while문을 돌리기 위한 초기값 설정
page_num = 1
while True:
    # 현재 페이지 url 생성
    url = url_template + f'&start={page_num}1'

    # requests 모듈을 사용하여 html 코드 가져오기
    response = requests.get(url)
    html = response.text

    # BeautifulSoup 모듈을 사용하여 html 코드 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 스크래핑할 데이터 추출
    articles = soup.select('ul.list_news > li')

    # 추출한 데이터 출력
    for article in articles:
        title = article.select_one('a.news_tit').text
        link = article.select_one('a.news_tit')['href']
        print(title, link)

    # 다음 페이지로 넘어가기 위한 조건문
    next_button = soup.select_one(".btn_next")
    if not next_button:
        break

    # 다음 페이지로 넘어가기 위한 초기값 설정
    page_num += 1