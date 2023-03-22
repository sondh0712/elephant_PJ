# 네이버 금융 가격 뽑기
# requests 라이브러리 사용
import requests as re

# 네이버 삼성전자 url 가져오기 
url="https://finance.naver.com/item/main.naver?code=005930"
data=re.get(url) #get()함수를 가장 많이 사용한다.
print(data.text)

