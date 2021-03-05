#-*- coding:utf-8 -*-
from tkinter import *
import tkinter.ttk
from pandastable import Table
import pandas as pd
import requests


#전체주문 api
url = "http://playauto-api.playauto.co.kr/emp/v1/orders"

querystring = {"startDate":"20210220","endDate":"20210305","count":"10"}
headers = {
    'user-agent': "vscode-restclient",
    'x-api-key': "0805a02bb9f1318cef8da503a4b7e05c"
    }
 
response = requests.request("GET", url, headers=headers, params=querystring)

res_json = response.json()

df = pd.json_normalize(res_json)
df1 = df.drop({"UniqueId","SiteCode"},axis = "columns") #,"OptCode"
df1.columns = ["DB번호","사이트","ID","사용자","수집일","주문일","결제일","송장전송일","상태변경일","배송예정일","상태","주문번호","상품코드","상품명","옵션명","옵션가",\
               "추가옵션","추가옵션가","원가","공급가","판매가","수량","배송방법","배송비","주문자아이디","주문자","주문자전화번호","주문자핸드폰","주문자이메일","수령자","수령자영문이름",\
               "수령자전화번호","수령자핸드폰","수령자우편번호","수령자주소","배송메세지","배송사","송장번호","마스터상품코드","판매자상품코드","기타메세지","주문자아이디","사은품",\
               "수령자주민등록번호(통관용)","그룹키"]

#메인
root=Tk()
root.title("Formongde")
root.geometry("1000x800")
root.resizable(True, True)

#노트북
ntb = tkinter.ttk.Notebook(root,height=1800)
ntb.pack(fill="both")

# ntb = ttk.Notebook()

#프레임1의 내용
frame1 = Frame(root, relief="solid", bd=1)
frame1.pack(fill="both", expand=True)
ntb.add(frame1,text='홈')

od_box = Listbox(frame1,bg="#FFFFF0",selectbackground="#FFFFF0") #,bg="#BC8F8F"
od_box.place(x=10, y=10)
td_od_lb = Label(od_box, text="오늘주문")
td_od_lb.grid(row=1, column=1)
td_od_lb2 = Label(od_box, text="680 건")
td_od_lb2.grid(row=2, column=1)
td_od_lb3 = Label(od_box, text="33,402,600 원")
td_od_lb3.grid(row=3, column=1)

#frame2의 내용
frame2 = Frame(root, relief="solid", bd=1)
frame2.pack(fill="both", expand=True)
ntb.add(frame2, text="주문관리")

ent_btn = Button(frame2, text="전체보기")
ent_btn.grid(row=0, column=0)
new_btn = Button(frame2, text="신규주문")
new_btn.grid(row=0, column=1)
cf_btn = Button(frame2, text="주문확인")
cf_btn.grid(row=1, column=1)
pt_btn = Button(frame2, text="보류")
pt_btn.grid(row=2, column=1)
op_btn = Button(frame2, text="송장출력")
op_btn.grid(row=0, column=2)
ip_btn = Button(frame2, text="송장입력")
ip_btn.grid(row=1, column=2)
rl_btn = Button(frame2, text="출고")
rl_btn.grid(row=2, column=2)
dl_btn = Button(frame2, text="배송중")
dl_btn.grid(row=0, column=3)
rc_btn = Button(frame2, text="수취확인")
rc_btn.grid(row=1, column=3)
cn_btn = Button(frame2, text="취소")
cn_btn.grid(row=2, column=3)
re_btn = Button(frame2, text="반품요청")
re_btn.grid(row=0, column=4)
ex_btn = Button(frame2, text="교환요청")
ex_btn.grid(row=1, column=4)

#frame3의 내용
frame3 = Frame(root, relief="solid", bd=1)
frame3.pack(fill="both", expand=True)
ntb.add(frame3, text="재고관리")

#데이터테이블
# ent_order_pt = Table(frame2, dataframe=df1)
# ent_order_pt.show()

root.mainloop()
