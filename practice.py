from tkinter import *
from pandastable import Table
import pandas as pd

#, "" : ""
df1 = pd.DataFrame({"A" : ["리버시블 낮잠 깜선인장", "세탁베개솜: 02와이드솜 30x50"],
                    "B" : ["리버시블낮잠 깜선인장", "와이드솜 30x50"]})

df2 = pd.DataFrame({"A" : ["포몽드 리버시블 순면 낮잠이불 순면리버시블 01깜선인장", "세탁베개솜: 02와이드솜 30x50"]}, index=(0,1)) #주문서의 옵션명

df3 = pd.DataFrame({"A":["리버시블낮잠 깜선인장"],
                    "B":["제품: 리버시블 낮잠이불, 선택: 깜선인장"],
                    "C":["포몽드 리버시블 순면 낮잠이불 순면리버시블 01깜선인장"]
                  })

fd = df3.loc[df3["C"].str.contains(df2.iloc[0,0])].A.values #정상
print(fd)

print(df3.loc[df3.loc[:,["A","B","C"]].str.contains(df2.iloc[0,0])].A.values)
# print(df3.iloc[0].str.contains(df2.loc[A]))
# print(df2["A"])
# print(df3.iloc[0])