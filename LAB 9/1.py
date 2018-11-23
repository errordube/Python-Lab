from Tkinter import *
from tkMessageBox import *
import sqlite3
root=Tk()
con=sqlite3.Connection("mydb")
cur=con.cursor()
cur.execute("create table if not exists emp(code number primary key,fname varchar2(20),lname varchar2(20))")

Label(root,text="Employee Record Keeping System :").grid(row=0,column=0)
Label(root,text="enter emp code :").grid(row=1,column=0)
Label(root,text="enter first name:").grid(row=2,column=0)
Label(root,text="enter last name:").grid(row=3,column=0)
Label(root,text="enter id to fetch record :").grid(row=4,column=0)

code=Entry(root)
code.grid(row=1,column=1)
fname=Entry(root)
fname.grid(row=2,column=1)
lname=Entry(root)
lname.grid(row=3,column=1)
eid=Entry(root)
eid.grid(row=4,column=1)

def insert():
    
    while True:
        try:
            cur.execute("insert into emp values(?,?,?)",(code.get(),fname.get(),lname.get()))
            con.commit()
            
            showinfo('Congrats','Successfully Inserted')
            break
        except sqlite3.IntegrityError:
            showerror('Error','Already Inserted')
            break
def show():
    cur.execute("select * from emp where code= "+(eid.get()))
    x=cur.fetchall()
    Label(root,text=x).grid(row=6,column=1)
    showinfo('Search',x)
def showall():
    cur.execute("select * from emp ")
    j=10
    a=cur.fetchall()
    for i in a:
        Label(root,text=str(i)).grid(row=j,column=1)
        j=j+1
        
Button(root,text="Insert",font='10',command=insert).grid(row=5,column=0)
Button(root,text="Show",font='10',command=show).grid(row=5,column=1)
Button(root,text="Showall",font='10',command=showall).grid(row=5,column=2)

root.mainloop()
