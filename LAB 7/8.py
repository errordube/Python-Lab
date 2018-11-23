from Tkinter import *
root=Tk()
Label(root,text='Enter Fno').grid(row=0,column=0)
fno=Entry(root)
fno.grid(row=0,column=1)
Label(root,text='Enter Sno').grid(row=1,column=0)
sno=Entry(root)
sno.grid(row=1,column=1)
def sum():
    Label(root,text=int(fno.get())+int(sno.get())).grid(row=7,column=0)
def diff():
    Label(root,text=int(fno.get())-int(sno.get())).grid(row=7,column=0)
def mul():
    Label(root,text=int(fno.get())*int(sno.get())).grid(row=7,column=0)
def div():
    Label(root,text=float(fno.get())/int(sno.get())).grid(row=7,column=0)
def rem():
    Label(root,text=int(fno.get())%int(sno.get())).grid(row=7,column=0)
Button(root,text="SUM",command=sum).grid(row=2,column=0)
Button(root,text="Diff",command=diff).grid(row=3,column=0)
Button(root,text="Multi",command=mul).grid(row=4,column=0)
Button(root,text="Div",command=div).grid(row=5,column=0)
Button(root,text="remainder",command=rem).grid(row=6,column=0)
root.mainloop()
