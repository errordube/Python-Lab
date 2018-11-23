PI=3.14
def Area_Circle(d,PI):
    
    r=d/2
    AC=PI*r*r
    return(AC)
d=input('Enter diameter value: ')
AC=Area_Circle(d,PI)
print("Area of Circle is: ",AC)
    
