def Area_Rectpri(w,h,l):
    ARP=2*(w*l+h*l+h*w)
    return(ARP)
w,h,l=input('Enter W,H,L value: ')
ARP=Area_Rectpri(w,h,l)
print("Area of Rectangular prism is: ",ARP)
