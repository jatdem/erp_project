#-*- coding:utf-8 -*- 
import requests
from pprint import pprint


import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

url = "http://playauto-api.playauto.co.kr/emp/v1/orders"

querystring = {"count":"500"}
headers = {
    'user-agent': "vscode-restclient",
    'x-api-key': "0805a02bb9f1318cef8da503a4b7e05c"
    }
 
response = requests.request("GET", url, headers=headers, params=querystring)
# response = requests.request("GET", url, headers=headers)
res_json = response.json()

df = pd.json_normalize(res_json)
df1 = df.drop({"UniqueId","SiteCode","OptCode"},axis = "columns")
df1.columns = ["DB번호","사이트","ID","사용자","수집일","주문일","결제일","송장전송일","상태변경일","배송예정일","상태","주문번호","상품코드","상품명","옵션명","옵션가","추가옵션","추가옵션가","원가","공급가","판매가","수량","배송방법","배송비","주문자아이디","주문자","주문자전화번호","주문자핸드폰","주문자이메일","수령자","수령자영문이름","수령자전화번호","수령자핸드폰","수령자우편번호","수령자주소","배송메세지","배송사","송장번호","마스터상품코드","판매자상품코드","기타메세지","주문자아이디","사은품","수령자주민등록번호(통관용)","그룹키"]


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = pandasModel(df1)
    view = QTableView()
    view.setModel(model)
    view.resize(800, 600)
    view.show()
    sys.exit(app.exec_())