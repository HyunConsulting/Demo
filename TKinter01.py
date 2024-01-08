from tkinter import *
from datetime import datetime
import requests
from bs4 import BeautifulSoup
def get_lotto():
    n = ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    req = requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    txts = soup.find("div",attrs={"class","win_result"}).get_text()
    num_list = txts.split("\n")[7:13]
    bonus =  txts.split("\n")[-4]
    print(num_list)
    print(bonus)

# def date_time_01():
#     btn.config(text=datetime.now())

# print(Tk().image_types)
win = Tk()
win.geometry("500x500")
win.configure(bg="blue")
win.title("Lotto")
win.option_add("*Font","맑은고딕 10")

ent = Entry(win)
ent.pack()

btn = Button(win)
btn.config(width=10)
btn.config(text="당첨번호확인")
btn.config(command=get_lotto)

btn.pack()

win.mainloop()