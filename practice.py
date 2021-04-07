from tkinter import *
import pandas as pd
import numpy as np

df1 = pd.DataFrame({"A" : ["리버시블 낮잠 깜선인장", "세탁베개솜: 02와이드솜 30x50"],
                    "B" : ["리버시블낮잠 깜선인장", "와이드솜 30x50"]})

df2 = pd.DataFrame({"A" : ["리버시블 낮잠 깜선인장", "세탁베개솜: 02와이드솜 30x50"]}, index=(0,1))


change = pd.read_excel("문자바꾸기.xlsx","바꾸기", na_values=[""]) #, index_col=None, na_values=[""]
order = pd.read_excel("문자바꾸기.xlsx","주문서", na_values=[""])

# print(df2[df2["A"] == "리버시블 낮잠 깜선인장"].values)
test = list(df1.loc[df1["A"].str.contains(df2.iloc[0,0])].B.values) #####같은 문자를 찾아서 바꿔주기 최종

# print(df1)
i = order.iloc[0,0]
fd = i.replace(i,str(change[change["찾을문자"]==i].바꿀문자.values))
new_df = pd.DataFrame({"제품명":[fd]})

i2 = order.iloc[1,0]
fd2 = pd.DataFrame({"제품명":[i2.replace(i2,str(change[change["찾을문자"]==i2].바꿀문자.values))]})
fd3 = new_df.append(fd2)

print(fd3)
