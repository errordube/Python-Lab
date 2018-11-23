from Tkinter import *
root=Tk()
e=Entry(root)
e.pack()
def fun():
    print e.get()
Button(root,text='Press',command=fun).pack()
root.mainloop()
