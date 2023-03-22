# 네이버 금융 가격 뽑기
# requests 라이브러리 사용
import requests as re
from bs4 import BeautifulSoup


# 네이버 삼성전자 url 가져오기 
url="https://finance.naver.com/item/main.naver?code=005930"

res=re.get(url)
#get()함수를 가장 많이 사용한다.

bsobj=BeautifulSoup(res.text,"html.parser")
#res텍스트를 변수에 저장
div_today = bsobj.find("div",{"class":"today"})
# div 이고 class명이 today이인것들을 찾아
em = div_today.find("em")
price = em.find("span",{"class":"blind"}).text


print(price)
#삼성전자 주식 가격만 가져오기

