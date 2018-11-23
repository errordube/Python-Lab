from Tkinter import *
root=Tk()
Label(root,text='Enter P').grid(row=0,column=0)
p=Entry(root)
p.grid(row=0,column=1)
Label(root,text='Enter R').grid(row=1,column=0)
r=Entry(root)
r.grid(row=1,column=1)
Label(root,text='Enter T').grid(row=2,column=0)
t=Entry(root)
t.grid(row=2,column=1)
def fun():
    Label(root,text=int(p.get())*float(r.get())*int(t.get())/100).grid(row=4,column=0)
    
Button(root,text='Simple Interest',command=fun).grid(row=3,column=0)

root.mainloop()
