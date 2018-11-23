














from Tkinter import *
import sqlite3
from datetime import datetime,date
root=Tk()
con=sqlite3.Connection("stud")
cur=con.cursor()
cur.execute('''DROP TABLE IF EXISTS stud''')
cur.execute("create table if not exists stud(roll_number number primary key, fname varchar2(20), lname varchar2(20), dob date, father varchar2(30), course varchar2(30), dept varchr2(30), r_date date, s_add varchar2(30), s_mob number, s_email varchar2(40), cgpa number, hobbies varchar2(40), certification varchar2(30))")

Label(root,text="Student Record Keeping System",font='10').grid(row=0,column=0)
Label(root,text="Enrollment:").grid(row=1,column=0)
Label(root,text="First Name:").grid(row=2,column=0)
Label(root,text="Last Name:").grid(row=3,column=0)
Label(root,text="DOB(YYYY-M-D):").grid(row=4,column=0)
Label(root,text="Father Name:").grid(row=5,column=0)
Label(root,text="Course(CSE/ECE/MECH/CIVIL):").grid(row=6,column=0)
Label(root,text="Dept:").grid(row=7,column=0)
Label(root,text="Registration Date:").grid(row=8,column=0)
Label(root,text="Student Address:").grid(row=9,column=0)
Label(root,text="Student Mobile:").grid(row=10,column=0)
Label(root,text="CGPA:").grid(row=11,column=0)
Label(root,text="Hobbies:").grid(row=12,column=0)
Label(root,text="Certification(RHCE/MCSE/CCNA/OCP):").grid(row=13,column=0)
Label(root,text="Enter Roll Number to fetch:").grid(row=14,column=0)

roll_number=Entry(root)
roll_number.grid(row=1,column=1)
fname=Entry(root)
fname.grid(row=2,column=1)
lname=Entry(root)
lname.grid(row=3,column=1)
dob=Entry(root)
dob.grid(row=4,column=1)
father=Entry(root)
father.grid(row=5,column=1)
course=Entry(root)
course.grid(row=6,column=1)
dept=Entry(root)
dept.grid(row=7,column=1)
r_date=Entry(root)
r_date.grid(row=8,column=1)
s_add=Entry(root)
s_add.grid(row=9,column=1)
s_mob=Entry(root)
s_mob.grid(row=10,column=1)
s_email=Entry(root)
s_email.grid(row=11,column=1)
cgpa=Entry(root)
cgpa.grid(row=12,column=1)
hobbies=Entry(root)
hobbies.grid(row=13,column=1)
certification=Entry(root)
certification.grid(row=14,column=1)
rid=Entry(root)
rid.grid(row=15,column=1)

def insert():
    cur.execute("insert into stud values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(roll_number.get(),fname.get(),lname.get(),dob.get(),father.get(),course.get(),dept.get(),r_date.get(),s_add.get(),s_mob.get(),s_email.get(),cgpa.get(),hobbies.get(),certification.get()))
    con.commit()
def show():
    cur.execute("select * from stud where roll_number= "+(rid.get()))
    Label(root,text=cur.fetchall()).grid(row=17,column=1)
def showall():
    cur.execute("select * from stud")
    j=20
    a=cur.fetchall()
    for i in a:
        Label(root,text=str(i)).grid(row=j,column=1)
        j=j+1
    


Button(root,text="Insert",command=insert).grid(row=16,column=0)
Button(root,text="Show",command=show).grid(row=16,column=1)
Button(root,text="Showall",command=showall).grid(row=16,column=2)



root.mainloop()
