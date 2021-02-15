import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("window.ui")[0] #ui파일 연결

class WindowClass(QMainWindow, form_class) : #화면을 띄우는데 사용되는 Class 선언
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    app = QApplication(sys.argv) #QApplication : 프로그램을 실행시켜주는 클래스
    myWindow = WindowClass() #WindowClass의 인스턴스 생성
    myWindow.show() #프로그램 화면을 보여주는 코드
    app.exec_() #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드