
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 검색어와 검색 기간 설정
query = '삼성전자'
start_date = datetime.now() - timedelta(weeks=1) # 2023-04-25 14:49:23.322423 / 타입 : class 'datetime.datetime'
end_date = datetime.now() # 2023-05-02 14:49:23.322423 / 타입 : class 'datetime.datetime'
# 검색 기간 URL 생성
start_date_str = start_date.strftime('%Y.%m.%d') # 2023-04-25 14:50:04.264278 / 타입 : string
end_date_str = end_date.strftime('%Y.%m.%d') # 2023-05-02 14:50:04.264278 / 타입 : string
# sort = 1 : 최신순, 
url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds={start_date_str}&de={end_date_str}&docid=&nso=so%3Add%2Cp%3Afrom{start_date_str.replace(".", "")}to{end_date_str.replace(".", "")}%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
# print(url) # url 확인

# HTTP 요청 보내기
response = requests.get(url)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 기사 제목과 링크 가져오기
def get_articles():
    articles = []
    for item in soup.select('.list_news .news_wrap .news_area'):
        title = item.select_one('.news_tit').text
        link = item.select_one('.news_tit')['href']
        articles.append({'title': title, 'link': link})

    # 결과 출력
    for article in articles:
        print(article['title'])
        print(article['link'])
        print('-' * 50)
    
# get_articles()

'''
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

start_date = datetime.now() - timedelta(weeks=1) # 2023-04-25 14:49:23.322423 / 타입 : class 'datetime.datetime'
end_date = datetime.now() # 2023-05-02 14:49:23.322423 / 타입 : class 'datetime.datetime'
start_date_str = start_date.strftime('%Y.%m.%d') # 2023-04-25 14:50:04.264278 / 타입 : string
end_date_str = end_date.strftime('%Y.%m.%d') # 2023-05-02 14:50:04.264278 / 타입 : string

query = "테슬라"  # 검색어 입력
url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds={start_date_str}&de={end_date_str}&docid=&nso=so%3Add%2Cp%3Afrom{start_date_str.replace(".", "")}to{end_date_str.replace(".", "")}%2Ca%3Aall&mynews=0&refresh_start=0&related=0'
headers = {"User-Agent": "Mozilla/5.0"}

# 첫 페이지에서 뉴스 링크 수집
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
news_links = [link["href"] for link in soup.select(".news_tit a")]

# 다음 페이지에서 뉴스 링크 수집
while True:
    next_button = soup.select_one(".paging_next")
    if not next_button:
        break  # 마지막 페이지면 중단
    next_url = "https://search.naver.com" + next_button["href"]
    response = requests.get(next_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    news_links += [link["href"] for link in soup.select(".news_tit a")]
    print(news_links)
    

# 뉴스 기사 내용 스크래핑
# for link in news_links:
    # response = requests.get(link, headers=headers)
    # soup = BeautifulSoup(response.content, "html.parser")
    # news_title = soup.select_one(".tts_head").text.strip()
    # link = item.select_one('.news_tit')['href']
    # news_content = "\n".join(p.text.strip() for p in soup.select(".news_body p"))
    # print(news_title)
    # print(link)
'''