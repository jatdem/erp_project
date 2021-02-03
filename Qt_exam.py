import sys

from PyQt5.QtCore import QCoreApplication

from PyQt5.QtWidgets import QApplication, QMainWindow #QMainWindow = 메인 윈도우 라이브러리

from PyQt5.QtWidgets import QAction, QMenu #QMenu = 서브 메뉴를 만드는 라이브러리





class My_Window(QMainWindow):

    def __init__(self):

        super().__init__()

        self.My_window()

    def My_window(self):

        self.statusBar()  #상태표시줄을 생성함

        self.statusBar().showMessage("상태표시줄 입니다.")  #상태 표시줄에 문자열 출력



        menu = self.menuBar()  #메뉴바 객체(메뉴 그룹을 담을 수 있는)를 생성

        file_group_menu = menu.addMenu("파일") #메뉴그룹("파일")을 메뉴바에에 추가

        edit_group_menu = menu.addMenu("편집") #메뉴그룹("편집")을 메뉴바에에 추가



        file_exit = QAction("Exit",self) #앱을 종료하는 메뉴 객체 생성

        file_exit.setShortcut('Ctrl+Q') #해당 메뉴 객체의 단축키 지정

        file_exit.setStatusTip("앱이 종료 됩니다.")

        file_exit.triggered.connect(QCoreApplication.instance().quit)

        #triggered의 의미는 이 객체가 선택 되었을때. connect = 어떤 코드를 연결한다

        #QCoreApplication.instance().quit = 앱을 종료 시킴



        new_txt = QAction("텍스트 파일",self)

        new_py = QAction("파이썬 파일",self)



        file_new = QMenu("새 파일", self) #QMenu 객체 생성, Q메뉴는 메뉴 그릅 아래 들어가는 하위 메뉴 개념

        file_new.addAction(new_txt) #Qmenu 객체에 위에서 생성한 net_txt 액션을 추가

        file_new.addAction(new_py) #Qmenu 객체에 위에서 생성한 net_py 액션을 추가





        file_group_menu.addMenu(file_new) #위에서 생성한 QMenu 객체를 메뉴 그룹(file_new)에 추가한다

        file_group_menu.addAction(file_exit)  #'파일그룹에 'file_exit 하위 액션메뉴를 추가한다





        self.resize(500,500)

        self.show()



app = QApplication(sys.argv)

win = My_Window()

sys.exit(app.exec_())