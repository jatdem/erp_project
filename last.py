from tkinter import *
from pandastable import Table
import pandas as pd

#, "" : ""
df1 = pd.DataFrame({"A" : ["리버시블 낮잠 깜선인장", "세탁베개솜: 02와이드솜 30x50"],
                    "B" : ["리버시블낮잠 깜선인장", "와이드솜 30x50"]})

df2 = pd.DataFrame({"A" : ["리버시블 낮잠 깜선인장", "세탁베개솜: 02와이드솜 30x50"]}, index=(0,1)) #주문서의 옵션명


# fd = df1.find(df2.iloc[0,0])

fd = str(df1.loc[df1["A"].str.contains(df2.iloc[0,0])].B.values)

# def repl(rw_value, col_value=0):
#     if df1.A.str.contains(df2.iloc[rw_value, col_value]):
#         print(df1.iloc[])

# x = df2.replace(df2.iloc[1,0], df1.iloc[1,1]) # df2(주문서) 문자 바꾸기

def rep_order():
    # og_prodname = 0
    for i in df2.A:
        fd = str(df1.loc[df1["A"].str.contains(i)].B.values)
        print(fd)
          

rep_order()