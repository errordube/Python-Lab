from Tkinter import *
root = Tk()
Label(root,text='Select Your Gender: ').pack()
v1=IntVar()
r=Radiobutton(root,text='Male',variable=v1,value=1)
r.pack()
r1=Radiobutton(root,text='Female',variable=v1,value=2)
r1.pack()
r2=Radiobutton(root,text='Other',variable=v1,value=3)
r2.pack()
def choice():
    Label(root,text=v1.get()).pack()
Button(root,text='Submit',command=choice).pack()
root.mainloop()
