def Simple_Interest(p,r,t):
    SI=(p*r*t)/100
    return(SI)
p,r,t=input('Enter p,r,t values: ')
SI=Simple_Interest(p,r,t)
print("The Simple Interest is: ",SI)
