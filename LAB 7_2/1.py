from Tkinter import *
root = Tk()
Label(root,text='Temperature Conversion').grid(row=0,column=0)
v=Entry(root)
v.grid(row=0,column=1)
def convert():
    Label(root,text='Temperature in Fahrenheit: '+str(float(v.get())*1.8+32)).grid(row=2,column=0)
Button(root,text='convert',command=convert).grid(row=1,column=0)    
root.mainloop()
