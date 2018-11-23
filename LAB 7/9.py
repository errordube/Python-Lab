from Tkinter import *
root=Tk()
def funn():
    Label(root,text='Nice Job').pack()
def fun():
    Button(root,text='Go',command=funn).pack()
Button(root,text='Create',command=fun).pack()
root.mainloop()
