from Tkinter import *
from tkMessageBox import *
root=Tk()
Label(root,text='Click on button below').pack()
def fun():
    showinfo('hi','GoodMorning')
    showerror('error','Something Wrong')
    askyesno('response','Do you agree')
    askyesnocancel('response','Do you agree')
Button(root,text='Click',command=fun).pack()
mainloop()
