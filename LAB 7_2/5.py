from Tkinter import *
root=Tk()
Label(root,text='Your Personal Details',font='times 20 bold',bg='green').pack()
Label(root,text='Enter Your Name:').pack()
a=Entry(root)
a.pack()
Label(root,text='Enter Your DoB in DD/MM/YYYY:').pack()
dob=Entry(root)
dob.pack()
Label(root,text='Please Select Your Highest Qualification').pack()
v2=IntVar()
v3=IntVar()
v4=IntVar()
Checkbutton(root,text='BTech',variable=v2,onvalue=10).pack()
Checkbutton(root,text='MTech',variable=v3,onvalue=20).pack()
Checkbutton(root,text='PhD',variable=v4,onvalue=30).pack()
Label(root,text='Please Select Your Branch').pack()
v1=IntVar()
r=Radiobutton(root,text='CSE',variable=v1,value=1)
r.pack()
r1=Radiobutton(root,text='ECE',variable=v1,value=2)
r1.pack()
r2=Radiobutton(root,text='ME',variable=v1,value=3)
r2.pack()
r3=Radiobutton(root,text='CE',variable=v1,value=4)
r3.pack()
r4=Radiobutton(root,text='CHE',variable=v1,value=5)
r4.pack()
def choice():
    if(v2.get()==10):
        qual="BTech"
    elif(v3.get()==20):
        qual="MTech"
    elif(v4.get()==30):
        qual="PhD"
    if(v1.get()==1):
        branch='CSE'
    elif(v1.get()==2):
        branch='ECE'
    elif(v1.get()==3):
        branch='ME'
    elif(v1.get()==4):
        branch='CE'
    elif(v1.get()==5):
        branch='CHE'

    Label(root,text='You are '+str(a.get()+' '+ qual +' '+ branch )).pack()
    
    
Button(root,text='See Details',command=choice).pack()

root.mainloop()

