# -*- coding:utf-8 -*-
from tkinter import *
import tkinter.ttk as ttk
from pandastable import Table
import pandas as pd
import requests
from tkcalendar import DateEntry


# 전체주문 api
url = "http://playauto-api.playauto.co.kr/emp/v1/orders"

querystring = {"startDate": "20210220", "endDate": "20210305", "count": "10"}
headers = {
    'user-agent': "vscode-restclient",
    'x-api-key': "0805a02bb9f1318cef8da503a4b7e05c"
}

response = requests.request("GET", url, headers=headers, params=querystring)

res_json = response.json()

df = pd.json_normalize(res_json)
df1 = df.drop({"UniqueId", "SiteCode"}, axis="columns")  # ,"OptCode"
df1.columns = ["DB번호", "사이트", "ID", "사용자", "수집일", "주문일", "결제일", "송장전송일", "상태변경일", "배송예정일", "상태", "주문번호", "상품코드", "상품명", "옵션명", "옵션가",
               "추가옵션", "추가옵션가", "원가", "공급가", "판매가", "수량", "배송방법", "배송비", "주문자아이디", "주문자", "주문자전화번호", "주문자핸드폰", "주문자이메일", "수령자", "수령자영문이름",
               "수령자전화번호", "수령자핸드폰", "수령자우편번호", "수령자주소", "배송메세지", "배송사", "송장번호", "마스터상품코드", "판매자상품코드", "기타메세지", "주문자아이디", "사은품",
               "수령자주민등록번호(통관용)", "그룹키"]

# 메인
root = Tk()
root.title("Formongde")
root.geometry("1800x1000+50+5")
root.resizable(True, True)

# 노트북
ntb = ttk.Notebook(root, height=1800)
ntb.pack(fill="both")

# ntb = ttk.Notebook()

# ==================================홈 프레임1의 내용===================================
frame1 = Frame(root, relief="solid", bd=1)
frame1.pack(fill="both", expand=True)
ntb.add(frame1, text='홈')

od_box = Listbox(frame1, bg="#FFFFF0",
                 selectbackground="#FFFFF0")  # ,bg="#BC8F8F"
od_box.place(x=10, y=10)
td_od_lb = Label(od_box, text="오늘주문")
td_od_lb.grid(row=1, column=1)
td_od_lb2 = Label(od_box, text="680 건")
td_od_lb2.grid(row=2, column=1)
td_od_lb3 = Label(od_box, text="33,402,600 원")
td_od_lb3.grid(row=3, column=1)

#==================================주문관리 프레임2의 내용===================================
frame2 = Frame(root, relief="solid", bd=1)
frame2.pack(fill="both", expand=True)
ntb.add(frame2, text="주문관리")

ent_btn = Button(frame2, text="전체보기", height=4)  # 버튼배치 시작
new_btn = Button(frame2, text="신규주문", width=6)
cf_btn = Button(frame2, text="주문확인", width=6, height=1)
pt_btn = Button(frame2, text="보류", width=6, height=1)
op_btn = Button(frame2, text="송장출력", width=6, height=1)
ip_btn = Button(frame2, text="송장입력", width=6, height=1)
rl_btn = Button(frame2, text="출고", width=6, height=1)
dl_btn = Button(frame2, text="배송중", width=6, height=1)
rc_btn = Button(frame2, text="수취확인", width=6, height=1)
cn_btn = Button(frame2, text="취소", width=6, height=1)
re_btn = Button(frame2, text="반품요청", width=6, height=1)
ex_btn = Button(frame2, text="교환요청", width=6, height=1)
ent_btn.place(x=2, y=4)  # 버튼좌표 설정 시작
new_btn.place(x=63, y=0)
cf_btn.place(x=63, y=27)
pt_btn.place(x=63, y=54)
op_btn.place(x=118, y=0)
ip_btn.place(x=118, y=27)
rl_btn.place(x=118, y=54)
dl_btn.place(x=173, y=0)
rc_btn.place(x=173, y=27)
cn_btn.place(x=173, y=54)
re_btn.place(x=228, y=0)
ex_btn.place(x=228, y=27)

src_lb = Label(frame2, text="검색")  # 검색 레이블
date_lb = Label(frame2, text="날짜")  # 날짜 레이블
src_ent = Entry(frame2)  # 검색 창
date_ent1 = Entry(frame2, width=10)  # 날짜 창1
date_ent2 = Entry(frame2, width=10)  # 날짜 창2
src_lb.place(x=290, y=0)
src_ent.place(x=330, y=0)
date_lb.place(x=290, y=21)
date_ent1.place(x=330, y=21)
date_ent2.place(x=408, y=21)

src_btn = Button(frame2, text="검색시작", height=4)  # 텍스트 검색 버튼
src_btn.place(x=484)

st_list = Listbox(frame2)  # 사이트 프레임(라벨)
st_list.place(x=2, y=100, width=160, height=600)
st_list.insert(1, "씨제이")
st_list.insert(2, "롯데닷컴")
st_list.insert(3, "에이케이몰")
st_list.insert(4, "신세계통합")
st_list.insert(5, "네이버")
st_list.insert(6, "롯데아이몰")
st_list.insert(7, "11번가")
st_list.insert(8, "현대몰")
st_list.insert(9, "롯데온")
st_list.insert(10, "쿠팡")
st_list.insert(11, "자사몰")
st_list.insert(12, "위메프")
st_list.insert(12, "직접입력")

od_frame = LabelFrame(frame2, text="전체주문")  # 주문 프레임(라벨)
od_frame.place(x=170, y=100, width=1738)
ent_order_pt = Table(od_frame, dataframe=df1)  # 주문 데이터프레임 출력
ent_order_pt.show()

#==================================재고관리 프레임3의 내용===================================
frame3 = Frame(root, relief="solid", bd=1)  # 프레임3 생성
frame3.pack(fill="both", expand=True)
ntb.add(frame3, text="재고관리")

stock_list = Listbox(frame3, selectmode='extended') # 재고버튼 리스트박스(프레임)
stock_list.pack(side="left", fill="y")

stock_frame = LabelFrame(frame3)  # 라벨프레임 생성     # stock_frame = LabelFrame(frame3)  # 라벨프레임 생성
stock_frame.pack(fill="both")                          # stock_frame.place(x=145, width=1850, height=1000)                             
                                                                                    
def stock_table():  # 재고표 라벨프레임에 출력해주는 함수
    lb = Label(stock_frame, text="text example")
    lb.pack()

stock_button1 = Button(stock_list, text="완제품재고", command=stock_table) # 재고버튼생성
stock_button2 = Button(stock_list, text="원단재고")
stock_button3 = Button(stock_list, text="협력업체재고")
# stock_button4 = Button(frame3, text="")
# stock_button5 = Button(frame3, text="")
stock_button1.place(x=2, y=4)  # 버튼좌표 설정 시작
stock_button2.place(x=2, y=34)
stock_button3.place(x=2, y=64)

# def stock_table():  # 재고표 라벨프레임에 출력해주는 함수
#     pass



# menu_tv.bind("<ButtonRelese-1>", stock_table) # 트리뷰 클릭시 재고출력 바인딩

#==================================택배관리 프레임4의 내용===================================
frame4 = Frame(root, relief="solid", bd=1)
frame4.pack(fill="both", expand=True)
ntb.add(frame4, text="택배관리")

delivery_list = Listbox(frame4, selectmode='extended') # 재고버튼 리스트박스(프레임)
delivery_list.pack(side="left", fill="y")

delivery_frame = LabelFrame(frame4)  # 라벨프레임 생성     # stock_frame = LabelFrame(frame3)  # 라벨프레임 생성
delivery_frame.pack(fill="both")                          # stock_frame.place(x=145, width=1850, height=1000)                                                                                                             

delivery_button1 = Button(delivery_list, text="출고", command=stock_table) # 재고버튼생성
delivery_button2 = Button(delivery_list, text="송장")
delivery_button3 = Button(delivery_list, text="비고")
# stock_button4 = Button(frame3, text="")
# stock_button5 = Button(frame3, text="")
delivery_button1.place(x=2, y=4)  # 버튼좌표 설정 시작
delivery_button2.place(x=2, y=34)
delivery_button3.place(x=2, y=64)


root.mainloop()
