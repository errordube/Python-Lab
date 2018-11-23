def factorial(n):
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    return(fact)
n=input('Enter any value: ')
fact=factorial(n)
print("Fatorial of a number is: ",fact)
    
