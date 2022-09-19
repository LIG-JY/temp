# get 요청해보기
# 데이터 조회
from selenium import webdriver as wd
from webdriver_manager.chrome import ChromeDriverManager
# driver = wd.Chrome(ChromeDriverManager().install())
# url = "http://www.38.co.kr"
# driver.get(url)


# request로 response 받아오기
import requests
url_ = 'http://www.38.co.kr/html/forum/board/?o=v&code=389930&no=793&page=15'
response_ = requests.get(url_)


# 원하는 부분 알 수 있게 parcing하기
import bs4
from bs4 import BeautifulSoup
# soup = BeautifulSoup(response_.text, 'html.parser')


# 본문 추출 함수
def contents_extract(responseobj):
    contents_ = BeautifulSoup(responseobj.text, 'html.parser')
    selected = contents_.select('.readtext')
    readable_contents = BeautifulSoup(str(selected), 'html.parser')
    ans = str(readable_contents.get_text())
    return ans[1:-1]


# 제목 추출 함수
def title_extract(responseobj):
    title_ = BeautifulSoup(responseobj.text, 'html.parser')
    selected = title_.select('.title.break')
    readable_title = BeautifulSoup(str(selected), 'html.parser')
    return readable_title.get_text()


# 작성일 추출 함수
import re


def date_extract(responseobj):
    date_ = BeautifulSoup(responseobj.text, 'html.parser')
    date_example = date_.find(string=re.compile("작성일"))  # 정규 표현식 활용
    # return date_example
    return date_example[6:16]


# dataframe 만드는 함수
import pandas as pd


def make_df(start, end):
    links = []
    titles = []
    dates = []
    contents = []

    def make_raw_data(num):  # 종목코드에 따라 함수 돌리게 바꾸기.
        url = 'https://www.38.co.kr/html/forum/board/?o=v&code=279570&no=' + str(num)
        response = requests.get(url)
        error_check = BeautifulSoup(response.text, 'html.parser').select('script')
        if '해당글의 내용이 삭제되었습니다.' in str(error_check):  # 삭제된 글 조건문으로 확인
            return
        else:
            links.append(url)
            title = title_extract(response)
            titles.append(title)
            date = date_extract(response)
            dates.append(date)
            content = contents_extract(response)
            contents.append(content)
        return
    for post_num in range(start, end):
        make_raw_data(post_num)
    raw_dict = dict()
    raw_dict['titles'] = titles
    raw_dict['links'] = links
    raw_dict['dates'] = dates
    raw_dict['contents'] = contents
    return raw_dict
    # return pd.DataFrame(raw_dict)


df = pd.DataFrame(make_df(1, 192))  # dataframe으로 변환
df.to_csv('38케이뱅크_1~191.csv')  # 파일명 지정해서 csv로 저장


# temp = requests.get('https://www.38.co.kr/html/forum/board/?o=v&code=279570&no=200')
# temp_par = BeautifulSoup(temp.text, 'html.parser')
# test = str(temp_par.select('script'))
# if '해당글의' in test:
#     print(1)