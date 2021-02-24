#-*- coding:utf-8 -*-

import tkinter as tk
from pandastable import Table
import pandas as pd
import requests
import tkinter.ttk

#전체주문 api
url = "http://playauto-api.playauto.co.kr/emp/v1/orders"

querystring = {"startDate":"20210101","endDate":"20210224","count":"100"}
headers = {
    'user-agent': "vscode-restclient",
    'x-api-key': "0805a02bb9f1318cef8da503a4b7e05c"
    }
 
response = requests.request("GET", url, headers=headers, params=querystring)

res_json = response.json()

df = pd.json_normalize(res_json)
df1 = df.drop({"UniqueId","SiteCode","OptCode"},axis = "columns")
df1.columns = ["DB번호","사이트","ID","사용자","수집일","주문일","결제일","송장전송일","상태변경일","배송예정일","상태","주문번호","상품코드","상품명","옵션명","옵션가","추가옵션","추가옵션가","원가","공급가","판매가","수량","배송방법","배송비","주문자아이디","주문자","주문자전화번호","주문자핸드폰","주문자이메일","수령자","수령자영문이름","수령자전화번호","수령자핸드폰","수령자우편번호","수령자주소","배송메세지","배송사","송장번호","마스터상품코드","판매자상품코드","기타메세지","주문자아이디","사은품","수령자주민등록번호(통관용)","그룹키"]

#메인윈도우 생성
root = tk.Tk()
root.title('formongde')

#노트북생성
notebook = tk.ttk.Notebook(root, width = 1000, height = 1000)
notebook.pack(fill = "both")

#프레임생성
frame1 = tk.Frame(root, relief = "solid", bd=1)
frame1.pack(fill='both', expand=False)
notebook.add(frame1, text = "홈")

frame2 = tk.Frame(root, relief = "solid", bd=1)
frame2.pack(fill='both', expand=True)
notebook.add(frame2, text = "주문관리1")

frame3 = tk.Frame(root, relief = "solid", bd=1)
frame3.pack(fill='both', expand=True)
notebook.add(frame3, text = "주문관리2")

frame4 = tk.Frame(root, relief = "solid", bd=1)
frame4.pack(fill='both', expand=True)
notebook.add(frame4, text = "재고관리")



#판다스테이블 가져오기
pt = Table(frame2, dataframe=df1)
pt.show()

root.mainloop()