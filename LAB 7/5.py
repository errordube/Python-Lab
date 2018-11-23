from Tkinter import *
root=Tk()
def info():
    Label(root,text='Welcome\n').pack()
Button(root,text='GO',command=info).pack()
root.mainloop()
