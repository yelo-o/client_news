# -*- coding: utf-8 -*-
'''
import requests
from bs4 import BeautifulSoup

# 자료 저장할 딕셔너리 초기화
def dic_initialize(main_article_dic, commen_dic):
    main_article_dic = {
        '플랫폼' : [],
        '날짜' : [],
        '제목' : [],
        '내용' : [],
        'url' : []
    }

    commen_dic = {
        'url_origin' : [],
        '날짜' : [],
        '내용' : []
    }
    return main_article_dic, commen_dic

# 검색어, 년, 월에 따라 크롤링 후 저장
def getPeriodSoup(keyword, year, month, day_start, day_end):
    paramsPage = []
    news_main_url = 'https://search.naver.com/search.naver?'

    params = {
        'where' : 'news',
        'sm' : 'tab_srt',
        'sort' : 1,
        'query' : keyword,
        'start' : 1,

        'ds' : '{}.{}.01'.format(str(year).zfill(2), str(month).zfill(2)), #
        'de' : '{}.{}.31'.format(str(year).zfill(2), str(month).zfill(2)),
        'pd' : 3
    }
    resp = requests.get(news_main_url, params=params)
    soup = BeautifulSoup(resp.text)

    # 주어진 기간 내 article 개수
    total_article = int(''.join(soup.find))

'''

import requests

# GET 요청 보내기
response = requests.get('https://www.itworld.co.kr/news/287683')
print(response.text)

# POST 요청 보내기
# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://www.example.com/post', data=payload)
# print(response.text)
