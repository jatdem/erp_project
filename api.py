import requests
from pprint import pprint

url = "http://playauto-api.playauto.co.kr/emp/v1/orders/?count=1000"
#주문 100건 이상 나오게 하는 방법: 주소 뒤에 /? 추가 하고 파라미터(body sheme 추가)

querystring = {"count":"3000"}
headers = {
    'user-agent': "vscode-restclient",
    'x-api-key': "0805a02bb9f1318cef8da503a4b7e05c"
    }
 
response = requests.request("GET", url, headers=headers, params=querystring)
res_json = response.json()
pprint(res_json)

# pprint(response.text)

# with open("apitest.html", "w", encoding="utf-8") as f:
#     f.write(response.text)
