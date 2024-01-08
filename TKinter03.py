from tkinter import *
import random
from datetime import datetime

win = Tk()

win.title("Aim Game")
win.geometry("300x150")
win.option_add("*Font","궁서 10")

#Label
lab = Label(win)
lab.config(text="표적개수")
lab.grid(column=0, row=0, padx = 20, pady =20)

#Entry
ent = Entry(win)
ent.grid(column=1,row=0,padx=20,pady=20)
k = 1

def ran_btn0():
    global k
    if k <= num_t:
        k += 1
        btn.destroy()
        ran_btn()
    else:
        finish_t = datetime.now()
        dif_sec = (finish_t - start_t).total_seconds()
        btn.destroy()
        lab = Label(win)
        lab.config(text="Total Second " + str(dif_sec))
        lab.pack(pady=230)
def ran_btn():
    global btn
    btn = Button(win)
    btn.config(bg="red")
    btn.config(command=ran_btn0)
    btn.config(text = k)
    btn.place(relx=random.random(),rely=random.random())

def btn_f():
    global num_t
    global start_t
    num_t = int(ent.get())
    for wg in win.grid_slaves():
        wg.destroy()
    win.geometry("500x500")
    ran_btn()
    start_t = datetime.now()
#Button
btn=Button(win)
btn.config(text='시작')
btn.config(command = btn_f)
btn.grid(column=0,row=1,columnspan=2)





win.mainloop()