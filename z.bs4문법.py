'''
Bs4(Beautiful Soup 4)
Html 또는 xml구조에서 필요한 값만 뽑아주는'체

'''
from bs4 import BeautifulSoup as bs

f=open('ex.html','rt',encoding='utf-8').read() #HTML 파일 읽 문자열 리턴
soup= bs(f'html.parser') #Soup 객체 생성
#soup 객체를 이용하여 문서를 출력 prettify()를 통해 HTML 문서를 보기
#좋게 가공해준다.
print(soup.prettify())   

ul=soup.find("ul")
lis=ul.find("li")  #<li> 하나 뽑음
lis=ul.find_all("li") #리스트 형태로 <li> 들을 뽑음 

for li in lis:  #<li> 들을 뽑음
    print(li)
    

for li in lis:  #<li> 들dml 글씨만 뽑는다.
    print(li.text)
    
#=============    
lis=soup.find("li")  #<li> 하나 뽑음
lis=soup.find_all("li") #리스트 형태로 <li> 들을 뽑음 

#ul을 거치지 않고 가면 모든 li을 뽑는다.

    
    
    