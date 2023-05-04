import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

url_template = 'https://search.naver.com/search.naver?where=news&query=파이썬&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds=2023.04.26&de=2023.05.03&docid=&nso=so%3Add%2Cp%3Afrom20230426to20230503%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
print(url_template)

# while문을 돌리기 위한 초기값 설정
# page_num = 1
next_page_exist = True
articles = [] # 리스트 선언 및 초기화

while next_page_exist:
    # 페이지 요청
    res = requests.get(url_template)
    soup = BeautifulSoup(res.text, 'html.parser')

    # 다음 버튼이 있는지 확인
    next_button = soup.select_one(".btn_next") # class가 "btn_next"
    if next_button:
        # 다음 버튼이 있으면 다음 페이지로 이동
        # page_num += 1
        for item in soup.select('.list_news .news_wrap .news_area'):
            title = item.select_one('.news_tit').text # 제목 긁어오기
            print(title)
            link = item.select_one('.news_tit')['href'] # 링크 긁어오기
            print(link)
            articles.append({'title': title, 'link': link}) # 긁어온 제목과 링크 'articles' 라는 리스트에 딕셔너리 형태로 추가하기
        url = f"https://search.naver.com/search.naver{next_button['href']}"
    else:
        # 다음 버튼이 없으면 while문 종료
        next_page_exist = False
        # break
print(articles)