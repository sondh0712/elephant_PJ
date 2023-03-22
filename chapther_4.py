#chapther_3를 함수로 만들기
import requests as re
from bs4 import BeautifulSoup
'''
'''

def crawl(code1):
    #바뀌는 곳
    url = f"https://finance.naver.com/item/main.naver?code={code1}"
    #파라미터 code 추가후 url앞에 f를 붙여 코드를 넣을수 있게 해준다.
    #다음 url code="자리에 code 함수 입력"
    res=re.get(url)

    bsobj=BeautifulSoup(res.text,"html.parser")

    div_today = bsobj.find("div",{"class":"today"})

    em = div_today.find("em")
    #가격
    price = em.find("span",{"class":"blind"}).text
    #이름
    h_company = bsobj.find("div",{"class":"h_company"})
    name=h_company.a.text
    #코드
    div_description=h_company.find("div",{"class":"description"})
    code = div_description.span.text
    #거래량
    table_no_info=bsobj.find("table",{"class":"no_info"})
    tds=table_no_info.tr.find_all("td")
    volume=tds[2].find("span",{"class":"blind"}).text

    #딕셔너리로 묶기
    dic={"price":price,"name":name,"code":code,"volume":volume}

    return dic

dic = crawl("035720")
print(dic)



