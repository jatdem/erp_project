#-*- coding:utf-8 -*- 
import requests
from pprint import pprint
import pandas as pd
#주문 100건 이상 나오게 하는 방법: 주소 뒤에 /? 추가 하고 파라미터(body sheme 추가)
url = "http://playauto-api.playauto.co.kr/emp/v1/orders"

querystring = {"count":"10"}
headers = {
    'user-agent': "vscode-restclient",
    'x-api-key': "0805a02bb9f1318cef8da503a4b7e05c"
    }
 
response = requests.request("GET", url, headers=headers, params=querystring)
res_json = response.json()

df = pd.json_normalize(res_json)
df1 = df.drop({"UniqueId","SiteCode"},axis = "columns")
df1.columns = ["DB번호","사이트","ID","사용자","수집일","주문일","결제일","송장전송일","상태변경일","배송예정일","상태","주문번호","상품코드","상품명","옵션명","옵션가","추가옵션","추가옵션가","원가","공급가","판매가","수량","배송방법","배송비","주문자아이디","주문자","주문자전화번호","주문자핸드폰","주문자이메일","수령자","수령자영문이름","수령자전화번호","수령자핸드폰","수령자우편번호","수령자주소","배송메세지","배송사","송장번호","마스터상품코드","판매자상품코드","기타메세지","주문자아이디","사은품","수령자주민등록번호(통관용)","그룹키"]
pprint(df1)
# df1.to_excel('order_example.xlsx') #액셀파일 저장
# df.columns = df.columns.str.replace("Number","db번호") #컬럼명 바꾸기
# df = pd.DataFrame()
# print(pd.json_normalize(res_json)) #json 데이터 ->데이터프레임 변환
# pprint(res_json)
# pprint(response.text)
# with open("apitest.html", "w", encoding="utf-8") as f:
#     f.write(response.text) #html 저장
