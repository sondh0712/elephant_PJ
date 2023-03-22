#족목명 거래량등 다양한 정보 추출
import requests as re
from bs4 import BeautifulSoup


url="https://finance.naver.com/item/main.naver?code=005930"

res=re.get(url)

bsobj=BeautifulSoup(res.text,"html.parser")

div_today = bsobj.find("div",{"class":"today"})

em = div_today.find("em")

price = em.find("span",{"class":"blind"}).text
print("가격 "+price)
print("="*20)
h_company = bsobj.find("div",{"class":"h_company"})
name=h_company.a.text
#print(h_company.a.text) 으로 a 태그로 바로 가기 가능
print("이름 "+name)
print("="*20)
#이름 뽑기 완료
div_description=h_company.find("div",{"class":"description"})
code = div_description.span.text
print("코드 "+code)
print("="*20)

table_no_info=bsobj.find("table",{"class":"no_info"})
tds=table_no_info.tr.find_all("td")
volume=tds[2].find("span",{"class":"blind"}).text
#print(tds[2]) 3번째 td 찾기
print("거래량 "+volume)
print("="*20)


dic={"price":price,"name":name,"code":code,"volume":volume}
print(dic)
print("="*20)




