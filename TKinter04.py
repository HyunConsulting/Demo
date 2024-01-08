from tkinter import *
from tkinter.ttk import *

win = Tk()
win.geometry("500x500")
win.option_add("*Font","Arial 20")

#listbox
# lb = Listbox(win)
# lb.config(selectmode=MULTIPLE)
# lb.insert(0,"1번")
# lb.insert(1,"2번")
# lb.insert(2,"3번")
# lb.insert(3,"4번")
# lb.pack()

# #check button
# cv1 = IntVar()
# cb1 = Checkbutton(win,text="1번",variable=cv1)
# cb1.pack()

# #radio button
# rv = IntVar()
# rb1 = Radiobutton(win,text="1번",value=0,variable=rv)
# rb2 = Radiobutton(win,text="2번",value=1,variable=rv)
# rb3 = Radiobutton(win,text="3번",value=2,variable=rv)
# rb1.pack()
# rb2.pack()
# rb3.pack()

# #comobox
# cb = Combobox(win)
# cb_list = ['1','2','3']
# cb.config(values = cb_list)
# cb.pack()

# #spinbox
# sb = Spinbox(win)
# sb.config(from_=1,to=5)
# sb.pack()

#Scale
scale = Scale(win)
scale.config(length=100,from_=0,to=100, orient=HORIZONTAL)
scale.pack()

#Button
btn=Button(win)
btn.config(text="옵션선택")
def click():
    # text = lb.curselection()[0]
    lb_text=scale.get()
    lab.config(text=lb_text)
btn.config(command=click)
btn.pack()

#Label
lab = Label(win)
lab.pack()

win.mainloop()