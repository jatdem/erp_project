import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A' : ["제품=토퍼 낮잠이불 세트, 선택=04동화의숲","제품: 자수낮잠패드+베개커버(베개솜미포함) / 선택: 01치크고미"]})
                    



# df3 = df2.replace(df2.iloc[0,0], df2.iloc[0,1])

df2 = pd.read_excel("pyex.xlsx", "Sheet1", index_col=None)

# print(df)
print(df1)
