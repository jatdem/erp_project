import tkinter.ttk 
from tkinter import *

root = Tk()
root.title("formongde")
root.geometry("1200x700")
root.resizable(True, True)

#노트북 생성
notebook = tkinter.ttk.Notebook(root, width = 1000, height = 1000)
notebook.pack(fill = "both")
#페이지1(원주문서)
frame1 = tkinter.Frame(root)
notebook.add(frame1, text = "page1")

# frame1_1 = Frame(frame1)
# frame1_1.pack()

# odsearch = Entry(frame1_1, text = "주문검색")
# odsearch.pack()
# # odlabel = Label(frame1_1, text = "주문검색")
# odlabel.pack()
# #페이지2(원주문서)
# frame2 = tkinter.Frame(root)
# notebook.add(frame2, text = "page2")

# page_2 = tkinter.Label(frame2, text = "내용을 입력하세요")
# page_2.pack()
# #페이지3(원주문서)
# frame3 = tkinter.Frame(root)
# notebook.add(frame3, text = "page3")

# page_3 = tkinter.Label(frame3, text = "내용을 입력하세요")
# page_3.pack()
# #페이지4(원주문서)
# frame4 = tkinter.Frame(root)
# notebook.add(frame4, text = "page4")

# page_4 = tkinter.Label(frame4, text = "내용을 입력하세요")
# page_4.pack()


root.mainloop()