PI=3.14
def Vol_Cylinder(r,h,PI):
    VCy=PI*r*r*h
    return(VCy)
r,h=input('Enter R,H value: ')
VCy=Vol_Cylinder(r,h,PI)
print("Volume of Cylinder is: ",VCy)
