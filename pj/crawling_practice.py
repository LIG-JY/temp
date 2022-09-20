## get 요청해보기
## 데이터 조회
from selenium import webdriver as wd
from webdriver_manager.chrome import ChromeDriverManager
driver = wd.Chrome(ChromeDriverManager().install())
url = "http://www.38.co.kr"
driver.get(url)


## request로 response 받아오기
import requests
url_ = 'http://www.38.co.kr/html/forum/board/?o=v&code=389930&no=793&page=15'
response_ = requests.get(url_)
# print(response_)
# print(type(response_))
# print(type(response_.text))


## 원하는 부분 알 수 있게 parcing하기
import bs4
from bs4 import BeautifulSoup
soup = BeautifulSoup(response_.text, 'html.parser')
# print(type(soup))
# example = soup.find_all('span') ## html tag로 검색
# print(example)
# print(type(example))


# 본문 추출
example2 = soup.select('.readtext')
resoup = BeautifulSoup(str(example2), 'html.parser') # 다시 soup 객체로
# print(resoup)
# print(type(resoup))
# print(resoup.get_text("\n", strip = True)) # 본문 처럼 1줄 씩 print
# print(resoup.get_text()) # 연 달아서 출력
# print(type(resoup.get_text()))


# 본문 추출 함수
def contents_extract(responseobj):
    contents_ = BeautifulSoup(responseobj.text, 'html.parser')
    selected = contents_.select('.readtext')
    readable_contents = BeautifulSoup(str(selected), 'html.parser')
    ans = str(readable_contents.get_text())
    return ans[1:-1]


# title_example = soup.select('.title.break')
# print(title_example)
# title_example_re = BeautifulSoup(str(title_example), 'html.parser')
# print(title_example_re.get_text())


# 제목 추출 함수
def title_extract(responseobj):
    title_ = BeautifulSoup(responseobj.text, 'html.parser')
    selected = title_.select('.title.break')
    readable_title = BeautifulSoup(str(selected), 'html.parser')
    return readable_title.get_text()

# print(title(response_)) # test

# 작성일 추출
import re
# date_example = soup.find(string=re.compile("작성일")) #정규 표현식 활용
# print(date_example)
# print(date_example[6:16])


# 작성일 추출 함수
def date_extract(responseobj):
    date_ = BeautifulSoup(responseobj.text, 'html.parser')
    date_example = date_.find(string=re.compile("작성일"))  # 정규 표현식 활용
    # return date_example
    return date_example[6:16]

# print(date_extract(response_))


import pandas as pd

## dataframe 만드는 함수
def make_df(start, end):
    links = []
    titles = []
    dates = []
    contents = []
    def make_raw_data(num):
        url = 'https://www.38.co.kr/html/forum/board/?o=v&code=389930&no=' + str(num)
        response_ = requests.get(url)
        error_check = BeautifulSoup(response_.text, 'html.parser')
        if '해당글의 내용이 삭제되었습니다.' in str(error_check):  # 삭제된 글 조건문으로 확인
            return
        else:
            links.append(url)
            title = title_extract(response_)
            titles.append(title)
            date = date_extract(response_)
            dates.append(date)
            content = contents_extract(response_)
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


# example_df = pd.DataFrame(make_df(793, 1211))
# example_df.to_csv('793~1210.csv')

temp = requests.get('https://www.38.co.kr/html/forum/board/?o=v&table=CI64400&code=064400&no=56455')
print(temp)
print(BeautifulSoup(temp.text, 'html.parser'))

temp_par = BeautifulSoup(temp.text, 'html.parser')
if '해당글' in str(temp_par):
    print('Error')

