# -*- coding:utf-8 -*-
# import warnings
# warnings.filterwarnings("ignore", 'This pattern has match groups') # uncomment to suppress the UserWarning
from tkinter import *
from pandastable import Table
import pandas as pd



change = pd.read_excel("문자바꾸기.xlsx","바꾸기", na_values=[""]) #, index_col=None, na_values=[""]
order = pd.read_excel("문자바꾸기.xlsx","주문서", na_values=[""])

# fd = df1.find(df2.iloc[0,0])

# fd = str(df1.loc[df1["A"].str.contains(df2.iloc[0,0])].B.values)

# def repl(rw_value, col_value=0):
#     if df1.A.str.contains(df2.iloc[rw_value, col_value]):
#         print(df1.iloc[])
# x = df2.replace(df2.iloc[1,0], df1.iloc[1,1]) # df2(주문서) 문자 바꾸기



# df1[df1["A"]==i].B.values
def rep_order():
    # global lb
    new_df = pd.DataFrame({"제품명":[]})
    # og_prodname = 0
    for i in order.제품명:
        fd = pd.DataFrame({"제품명":[i.replace(i,str(change[change["찾을문자"]==i].바꿀문자.values))]})
        return new_df.append(fd)
    print(new_df)    

rep_order()

root = Tk()


lb = Label(root, text=order)
lb.pack()


btn = Button(root, text="button", command=rep_order)
btn.pack()



root.mainloop()