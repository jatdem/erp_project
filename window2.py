# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 912)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1111, 881))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 200, 1101, 651))
        self.frame.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.frame)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1080, 0, 16, 631))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.frame)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 630, 1081, 20))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 1071, 621))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(40, 7, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 33, 31, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 30, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(158, 7, 51, 41))
        self.pushButton.setObjectName("pushButton")
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setGeometry(QtCore.QRect(210, 10, 731, 181))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 71, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 10, 57, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 46, 57, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 80, 57, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 46, 57, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 10, 57, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(150, 80, 57, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 10, 57, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 46, 57, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 80, 57, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_12.setGeometry(QtCore.QRect(270, 10, 57, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_13.setGeometry(QtCore.QRect(270, 46, 57, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_14.setGeometry(QtCore.QRect(270, 80, 57, 31))
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_14.setTabletTracking(False)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_15.setGeometry(QtCore.QRect(330, 10, 57, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_16.setGeometry(QtCore.QRect(330, 46, 57, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_17.setGeometry(QtCore.QRect(330, 80, 57, 31))
        self.pushButton_17.setObjectName("pushButton_17")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 20, 1101, 831))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.frame_2)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(1080, 0, 16, 810))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.frame_2)
        self.horizontalScrollBar_2.setGeometry(QtCore.QRect(0, 812, 1080, 20))
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 921, 601))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.frame_3)
        self.verticalScrollBar_3.setGeometry(QtCore.QRect(900, 0, 16, 561))
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.horizontalScrollBar_3 = QtWidgets.QScrollBar(self.frame_3)
        self.horizontalScrollBar_3.setGeometry(QtCore.QRect(0, 571, 901, 20))
        self.horizontalScrollBar_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_3.setObjectName("horizontalScrollBar_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action1_2 = QtWidgets.QAction(MainWindow)
        self.action1_2.setObjectName("action1_2")
        self.action2_2 = QtWidgets.QAction(MainWindow)
        self.action2_2.setObjectName("action2_2")
        self.action3_2 = QtWidgets.QAction(MainWindow)
        self.action3_2.setObjectName("action3_2")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "검색"))
        self.label_2.setText(_translate("MainWindow", "날짜"))
        self.pushButton.setText(_translate("MainWindow", "검색"))
        self.pushButton_2.setText(_translate("MainWindow", "전체보기"))
        self.pushButton_3.setText(_translate("MainWindow", "신규주문"))
        self.pushButton_4.setText(_translate("MainWindow", "주문확인"))
        self.pushButton_5.setText(_translate("MainWindow", "보류"))
        self.pushButton_6.setText(_translate("MainWindow", "송장입력"))
        self.pushButton_7.setText(_translate("MainWindow", "송장출력"))
        self.pushButton_8.setText(_translate("MainWindow", "출고"))
        self.pushButton_9.setText(_translate("MainWindow", "배송중"))
        self.pushButton_10.setText(_translate("MainWindow", "수취확인"))
        self.pushButton_11.setText(_translate("MainWindow", "정산완료"))
        self.pushButton_12.setText(_translate("MainWindow", "취소"))
        self.pushButton_13.setText(_translate("MainWindow", "반품요청"))
        self.pushButton_14.setText(_translate("MainWindow", "교환요청"))
        self.pushButton_15.setText(_translate("MainWindow", "취소마감"))
        self.pushButton_16.setText(_translate("MainWindow", "반품마감"))
        self.pushButton_17.setText(_translate("MainWindow", "교환마감"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "주문관리"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "주문서정리"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "송장정리"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action3.setText(_translate("MainWindow", "3"))
        self.action1_2.setText(_translate("MainWindow", "1"))
        self.action2_2.setText(_translate("MainWindow", "2"))
        self.action3_2.setText(_translate("MainWindow", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
