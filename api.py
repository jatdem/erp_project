import requests

url = "http://playauto-api.playauto.co.kr/emp/v1/orders"

headers = {
    'user-agent': "vscode-restclient",
    'x-api-key': "0805a02bb9f1318cef8da503a4b7e05c"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
