import tkinter as tk
from tkinter import ttk
import datetime
from tkinter import messagebox
import csv
import sys
import pypyodbc as odbc

def getTimeNow(variant):
    if variant=='hms':
        time=datetime.datetime.now().strftime("%I:%M:%S %p")
    else:
        time=datetime.datetime.now().strftime("%I:%M %p")
    return time

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'HYUNCONSULTING'
DATABASE_NAME = 'DEMODB'
username = 'DEMODB_ADMIN'
password = 'jons00580*'

conn_string = f"""
    Driver={{{DRIVER_NAME}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    uid={username};
    pwd={password};
"""

def connection():
    try:
        conn = odbc.connect(conn_string)
    except Exception as e:
        print(e)
        print('task is terminated')
        sys.exit()
    else:
        return conn

def refreshTable():
    for data in treeview.get_children():
        treeview.delete(data)
    for array in read():
        treeview.insert('',tk.END,values=array[1:],iid=array[0])
        print(array)
    treeview.pack()


def read():
    conn = connection()
    cursor = conn.cursor()
    sql=f"SELECT id, e_id, name, time_in, time_out FROM dbo.python_time_in_out ORDER BY id DESC"
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def save(variant,e_id,password,time):
    conn = connection()
    cursor = conn.cursor()
    sql=f"SELECT * FROM dbo.python_employee where e_id = {e_id} and password = {password}"
    cursor.execute(sql)
    result=cursor.fetchall()
    conn.commit()
    conn.close()
    if not result:
        messagebox.showwarning("","Wrong employee id or password")
        return False
    name=result[2]
    conn = connection()
    cursor = conn.cursor() 
    sql=f"SELECT * FROM dbo.python_time_in_out where e_id = {e_id} AND time_out = '----'"
    cursor.execute(sql)
    result=cursor.fetchall()
    conn.commit()
    conn.close()
    if variant=='Time_In':
        if result:
            if result[4]=='----':
                messagebox.showwarning("","You're already Time_In")
                return True
        try:
            conn = connection()
            cursor = conn.cursor()
            sql=f"INSERT INTO Python_time_in_out (e_id, name, time_in, time_out) VALUES ({e_id}, {name}, {time}, '----')"
            cursor.execute(sql)
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showwarning("","Error while Time_In : "+e)
        refreshTable()
    else:
        if result:
            messagebox.showwarning("","You're already Time_Out")
            return True
        try:
            conn = connection()
            cursor = conn.cursor()
            sql=f"UPDATE dbo.python_time_in_out SET time_out = {time} WHERE e_id = {e_id}"
            cursor.execute(sql)
            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showwarning("","Error while Time_In : "+e)
        refreshTable()
    return True

 
def exportExcel():
    conn = connection()
    cursor = conn.cursor()
    sql=f"SELECT e_id, name, time_in, time_out FROM dbo..python_time_in_out ORDER BY id DESC"
    cursor.execute(sql)
    dataraw=cursor.fetchall()
    date = str(datetime.now())
    date = date.replace(' ', '_')
    date = date.replace(':', '-')
    dateFinal = date[0:16]
    with open("time_in_out_"+dateFinal+".csv",'a',newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in dataraw:
            w.writerow(record)
    print("saved: time_in_out_"+dateFinal+".csv")
    conn.commit()
    conn.close()
    messagebox.showinfo("","Excel file downloaded")

def clear():
    delete=messagebox.askyesno("","Are you sure you want to delete all records ?")
    if delete:
        conn = connection()
        cursor = conn.cursor()
        sql=f"DELETE FROM dbo.python_time_in_out"
        cursor.execute(sql)
        conn.commit()
        conn.close()
    refreshTable()



root = tk.Tk()
root.title("Check-in Check-out system")
style=ttk.Style(root)
root.tk.call("source","D:\Data\Python\Forest-ttk-theme-master\\forest-light.tcl")
root.tk.call("source","D:\Data\Python\Forest-ttk-theme-master\\forest-dark.tcl")
style.theme_use("forest-dark")
root.geometry("580x400")
root.resizable(False,False)

frame=ttk.Frame(root)
frame.pack()

widgets_frame=ttk.LabelFrame(frame,text="Manage")
widgets_frame.grid(row=0,column=0,padx=[10,5],pady=10,sticky="n")

def renderModal(variant):
    modal = tk.Tk()
    modal.title(f"{variant} Modal")
    style=ttk.Style(modal)
    modal.tk.call("source","D:\Data\Python\Forest-ttk-theme-master\\forest-light.tcl")
    modal.tk.call("source","D:\Data\Python\Forest-ttk-theme-master\\forest-dark.tcl")
    style.theme_use("forest-dark")
    modal.resizable(False,False)

    modalFrame=ttk.Frame(modal)
    modalFrame.pack()

    modalWidgetsFrame=ttk.LabelFrame(modalFrame,text=variant)  
    modalWidgetsFrame.grid(row=0,column=0,padx=20,pady=20)   

    e_idEntry=ttk.Entry(modalWidgetsFrame)
    e_idEntry.insert(0,"E_ID")
    e_idEntry.bind("<FocusIn>",lambda e:e_idEntry.delete('0','end'))
    e_idEntry.grid(row=0,column=0,padx=10,pady=[10,5],sticky="ew") 

    passwordEntry=ttk.Entry(modalWidgetsFrame)
    passwordEntry.insert(0,"Password")
    passwordEntry.bind("<FocusIn>",lambda e:passwordEntry.delete('0','end'))
    passwordEntry.grid(row=1,column=0,padx=10,pady=[0,5],sticky="ew") 

    timeEntry=ttk.Entry(modalWidgetsFrame)
    timeEntry.insert(0,getTimeNow('hm'))
    timeEntry.grid(row=2,column=0,padx=10,pady=[0,5],sticky="ew") 
    timeEntry.config(state="disabled") 

    submitBtn=ttk.Button(modalWidgetsFrame,text='Sumbit',command=lambda: submit(modal,variant,str(e_idEntry.get()),str(passwordEntry.get()),str(timeEntry.get())))
    submitBtn.grid(row=4,column=0,padx=10,pady=[0,5],sticky="nsew")

def submit(modal,variant,e_id,password,time):
    print(e_id,password,time)
    if not(e_id and e_id.strip()) or not(password and password.strip()) or e_id=='E_ID' or password=='Password':
        messagebox.showwarning("","Please fill up all entries")
        return
    if save(variant, e_id, password, time):
        modal.destroy()


buttonTimeIn=ttk.Button(widgets_frame,text="Time_In",command=lambda: renderModal("Time_In"))
buttonTimeIn.grid(row=0,column=0,padx=10,pady=[10,5],sticky="nsew")

buttonTimeOut=ttk.Button(widgets_frame,text="Time_Out",command=lambda: renderModal("Time_Out"))
buttonTimeOut.grid(row=1,column=0,padx=10,pady=[0,5],sticky="nsew")

buttonExcel=ttk.Button(widgets_frame,text="Download Excel",command=exportExcel)
buttonExcel.grid(row=2,column=0,padx=10,pady=[0,5],sticky="nsew")

buttonClear=ttk.Button(widgets_frame,text="Clear",command=clear)
buttonClear.grid(row=3,column=0,padx=10,pady=[0,5],sticky="nsew")

treeFrame=ttk.Frame(frame)
treeFrame.grid(row=0,column=1,padx=[5,10],pady=10,sticky="n",ipadx=5,ipady=5)

treeScroll=ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right",fill="y")

cols=("E_ID","Name","Time_In","Time_Out")
treeview=ttk.Treeview(treeFrame,show="headings",yscrollcommand=treeScroll.set,columns=cols,height=13)
treeview.heading("E_ID",text="E_ID",anchor="w")
treeview.heading("Name",text="Name",anchor="w")
treeview.heading("Time_In",text="Time_In",anchor="w")
treeview.heading("Time_Out",text="Time_Out",anchor="w")
treeview.column("E_ID",width=50)
treeview.column("Name",width=110)
treeview.column("Time_In",width=70)
treeview.column("Time_Out",width=70)

refreshTable()
treeScroll.config(command=treeview.yview)

def updateClock():
    realTimeClock.config(text=getTimeNow('hms'))
    realTimeClock.after(1000,updateClock)

realTimeClock=ttk.Label(text=getTimeNow('hms'),font=('Arial BOLD',20))
realTimeClock.pack(pady=[0,20])
realTimeClock.after(1000,updateClock)


root.mainloop()
