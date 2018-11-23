from Tkinter import *
root=Tk()
root.title('Welcome')
Label(root,text="Lab").pack()
name=Entry(root)
name.pack()
def fun():
    Label(root,text=name.get()+'Welcome to Python').pack()
Button(root,text='Press',command=fun).pack()
root.mainloop()
