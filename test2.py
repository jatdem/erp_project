import pandas as pd
import numpy as np
import re

df1 = pd.DataFrame({"A" : ["리버시블 낮잠 깜선인장", "세탁베개솜: 02와이드솜 30x50"],
                    "B" : ["리버시블낮잠 깜선인장", "와이드솜 30x50"]})
                  
# print("df1 데이터", df1)
print("")                    
# # rp_df1 = df1.replace(df2.iloc[0,0], df2.iloc[0,1])

df2 = pd.DataFrame({"A" : "리버시블 낮잠 깜선인장"}, index=(0,1))
print("df2 데이터", df2)

def repl(x):
    for i in len(df2["A"])
    if df2.iloc[0,0] == df1.iloc[0,0]:
        print(df2.replace(df2.iloc[0,0], df1.iloc[0,x]))