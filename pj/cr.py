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
# print(response_.text)

## 원하는 부분 알 수 있게 parcing하기
import bs4
from bs4 import BeautifulSoup
soup = BeautifulSoup(response_.text, 'html.parser')
example = soup.find('span') ## html tag로 검색

while example:
    print(example)
    example = example.next_sibling
