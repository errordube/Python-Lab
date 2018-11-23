def Compound_Interest(p,r,n,t):
    CI=p*(1+r/n)**(n*t)
    return(CI)
p,r,n,t=input('Enter P,R,N,T values: ')
CI=Compound_Interest(p,r,n,t)
print("Compound Interest is: ",CI)
