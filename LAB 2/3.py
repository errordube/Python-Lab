#Simple and Compound Interest
p = int(input('Enter Value of p: '))
r = int(input('Enter Value of r: '))
t = int(input('Enter Value of t: '))
n = int(input('Enter Value of n: '))
si = (p*r*t)/100
print(si)
ci = p*(1+r/n)**(n*t)
print(ci) 