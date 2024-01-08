from tkinter import *
win = Tk()
win.title("Log In 화면")
win.geometry("500x500")
win.option_add("*Font","궁서 20")

# LOGO
lab0 = Label(win)
img = PhotoImage(file = "D:/Data/Image/Login.png",master=win)
img = img.subsample(5)
lab0.config(image=img)
lab0.pack()

# ID 라벨
lab1 = Label(win)
lab1.config(text = "ID")
lab1.pack()
# ID 입력창
ent1 = Entry(win)
ent1.insert(0,"temp@gmail.com")
def clear(event):
    if ent1.get() == "temp@gmail.com":
        ent1.delete(0,len(ent1.get()))
ent1.bind("<Button-1>",clear)
ent1.pack()
# PW 라벨
lab2 = Label(win)
lab2.config(text = "PWD")
lab2.pack()
# PW 입력창
ent2 = Entry(win)
ent2.config(show="*")
ent2.pack()
# 로그인 버튼
btn = Button(win)
btn.config(text="로그인")
def login():
    my_id = ent1.get()
    my_pwd = ent2.get()
    print(my_id, my_pwd)
    lab3.config(text = "[메시지] log in 성공 !")

btn.config(command = login)
btn.pack()

# 메시지 라벨
lab3 = Label(win)
lab3.pack()

win.mainloop()

from selenium import webdriver
driver = webdriver.Chrome("D:/Data/HTML/chromedriver.exe")
