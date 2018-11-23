from Tkinter import *
from math import sqrt
root = Tk()
Label(root,text='Check Prime').pack()
v=Entry(root)
v.pack()
def prime():
    a=int(v.get())
    if(a==2):
         Label(root,text='Not Prime').pack()
    elif(a%2==0):
        Label(root,text='Not Prime').pack()
    else:
        i=3
        c=0
        while(i<sqrt(a)):
            if(a%1==0):
                c=1
            i+=2
        if(c==0):
            Label(root,text='Prime').pack()
        else:
             Label(root,text='Not Prime').pack()        
    
Button(root,text='Check',command=prime).pack()    
root.mainloop()
