import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# 1. 검색어 불러오기
with open('clients.txt', 'r', encoding='utf-8') as file:
    clients_list = [line.strip() for line in file]
print("클라이언트 리스트")
print(clients_list)
print('=' * 50)

# 검색어와 검색 기간 설정
query = '파이썬'
start_date = datetime.now() - timedelta(weeks=1) # 2023-04-25 14:49:23.322423 / 타입 : class 'datetime.datetime'
end_date = datetime.now() # 2023-05-02 14:49:23.322423 / 타입 : class 'datetime.datetime'
# 타입 변경 class -> str
start_date_str = start_date.strftime('%Y.%m.%d') # 2023-04-25 / 타입 : string
end_date_str = end_date.strftime('%Y.%m.%d') # 2023-05-02 / 타입 : string



def get_articles():
    page_num = 1
    next_page_exist = True


    while next_page_exist:
        # sort = 1 : 최신순, 
        url = f'https://search.naver.com/search.naver?where=news&query={query}&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds={start_date_str}&de={end_date_str}&docid=&nso=so%3Add%2Cp%3Afrom{start_date_str.replace(".", "")}to{end_date_str.replace(".", "")}%2Ca%3Aall&mynews=0&refresh_start=0&related=0' 
        print(url)

        # HTTP 요청 보내기
        response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
        html = response.text

        # BeautifulSoup 객체 생성
        soup = BeautifulSoup(html, 'html.parser')

    # 기사 제목과 링크 가져오기
        articles = [] # 리스트 선언 및 초기화
        next_button = soup.select_one(".btn_next")
    
        for item in soup.select('.list_news .news_wrap .news_area'):
            if next_button.has_attr("aria-disabled") and next_button["aria-disabled"] == "true":
                break # 다음 버튼이 비활성화되면 검색 중지
                
            else:
                url = "https://search.naver.com/search.naver" + next_button["href"]
                # HTTP 요청 보내기
                response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
                html = response.text
                # BeautifulSoup 객체 생성
                soup = BeautifulSoup(html, 'html.parser')
                title = item.select_one('.news_tit').text # 제목 긁어오기
                link = item.select_one('.news_tit')['href'] # 링크 긁어오기
                articles.append({'title': title, 'link': link}) # 긁어온 제목과 링크 'articles' 라는 리스트에 딕셔너리 형태로 추가하기
                
        print(articles)
        # 결과 출력
        # for article in articles:
            # print(article['title'])
            # print(article['link'])
            # print('-' * 50)
        
        # next_button = soup.select_one(".btn_next")


''' import requests
from bs4 import BeautifulSoup
# 검색 결과 페이지 URL
url = "https://search.naver.com/search.naver?where=news&query=파이썬&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=3&ds=2023.04.26&de=2023.05.03&docid=&nso=so%3Add%2Cp%3Afrom20230426to20230503%2Ca%3Aall&mynews=0&refresh_start=0&related=0"

while True:
    # 페이지 요청
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    # 다음 버튼이 비활성화 되어 있는지 확인
    next_button = soup.select_one(".btn_next")
    if next_button.has_attr("aria-disabled") and next_button["aria-disabled"] == "true":
        break
'''

'''        
    # 다음 페이지 URL 생성
    url = "https://search.naver.com" + next_button["href"]

        
# 다음 페이지로 이동 (다음 페이지 버튼이 비활성화될 때까지)
next_button = soup.select_one(".btn_next")
print(next_button)

while True:
    next_button = soup.select_one(".btn_next")
    if not next_button:
        break  # 마지막 페이지면 중단
    next_url = "https://search.naver.com" + next_button["href"]
    print(next_url)
    response = requests.get(next_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    news_links += [link["href"] for link in soup.select(".news_tit a")]
    print(news_links)
'''
# 2. 


# 실행
get_articles()




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
