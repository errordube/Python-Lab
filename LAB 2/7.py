#Swap of two numbers without using third variable
a=int(input('Enter Value of first: '))
b=int(input('Enter Value of second: '))
a = a+b
b = a-b
a = a-b
print("a is: ",a,"b is: ",b)
