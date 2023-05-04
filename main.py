import pandas as pd # pandas 모듈을 불러온다.
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 1. 검색어 불러오기
with open('clients.txt', 'r', encoding='utf-8') as file:
    clients_list = [line.strip() for line in file]
print("클라이언트 리스트는 아래와 같습니다.")
print(clients_list)
print('=' * 50)

# clients_list에 있는 검색어를 하나씩 대입하여 모든 페이지를 스크래핑
for client in clients_list:
    # 검색어와 검색 기간 설정
    query = client
    start_date = datetime.now() - timedelta(weeks=1) # 2023-04-25 14:49:23.322423 / 타입 : class 'datetime.datetime'
    end_date = datetime.now() # 2023-05-02 14:49:23.322423 / 타입 : class 'datetime.datetime'
    # 타입 변경 class -> str
    start_date_str = start_date.strftime('%Y.%m.%d') # 2023-04-25 / 타입 : string
    end_date_str = end_date.strftime('%Y.%m.%d') # 2023-05-02 / 타입 : string


    # 기사 보관 리스트 생성
    article_list = []

    # 스크래핑할 첫 페이지 url
    url_template = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds={start_date_str}&de={end_date_str}&docid=&nso=so%3Add%2Cp%3Afrom{start_date_str.replace(".", "")}to{end_date_str.replace(".", "")}%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
    # print(url_template)

    response = requests.get(url_template, headers={'User-Agent':'Mozilla/5.0'})
    html = response.text
    # BeautifulSoup 모듈을 사용하여 html 코드 파싱
    soup = BeautifulSoup(html, 'html.parser')

    # 스크래핑할 데이터 추출
    articles = soup.select('ul.list_news > li')

    # 추출한 데이터 출력
    for article in articles:
        title = article.select_one('a.news_tit').text
        link = article.select_one('a.news_tit')['href']
        article_list.append({'제목': title, '링크': link}) # 긁어온 제목과 링크 'articles' 라는 리스트에 딕셔너리 형태로 추가하기

    # 2 ~ 마지막 페이지 스크래핑

    # while문을 돌리기 위한 초기값 설정
    page_num = 1
    while True:
        # 현재 페이지 url 생성
        url = url_template + f'&start={page_num}1'
        # print(url)
        # requests 모듈을 사용하여 html 코드 가져오기
        response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
        html = response.text

        # BeautifulSoup 모듈을 사용하여 html 코드 파싱
        soup = BeautifulSoup(html, 'html.parser')

        # 스크래핑할 데이터 추출
        articles = soup.select('ul.list_news > li')

        # 추출한 데이터 출력
        for article in articles:
            title = article.select_one('a.news_tit').text
            link = article.select_one('a.news_tit')['href']
            article_list.append({'제목': title, '링크': link}) # 긁어온 제목과 링크 'articles' 라는 리스트에 딕셔너리 형태로 추가하기

        # 다음 페이지로 넘어가기 위한 조건문
        next_button = soup.select_one(".btn_next")
        if not next_button:
            break

        # 다음 페이지로 넘어가기 위한 초기값 설정
        page_num += 1
        

    df = pd.DataFrame(article_list)  # 딕셔너리를 데이터프레임으로 변환한다.
    df.to_excel(f'{query}.xlsx', index=False) # 데이터프레임을 엑셀 파일로 저장한다.
