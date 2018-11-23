a,b,c,d,e,f,g,h,i,j=(input('Enter the 1-10 integers: '))
if a%2 ==0:
    a = 0  
else:
    a = a 
if b%2 ==0:
    b = 0 
else:
    b = b
if c%2 ==0:
    c = 0
else:
    c = c 
if d%2 ==0:
    d = 0
else:
    d = d
if e%2 ==0:
    e = 0
else:
    e = e
if f%2 ==0:
    f = 0
else:
    f = f
if g%2 ==0:
    g = 0
else:
    g = g
if h%2 ==0:
    h = 0
else:
    h = h
if i%2 ==0:
    i = 0 
else:
    i = i 
if j%2 ==0:
    j = 0  
else:
    j = j
value = a,b,c,d,e,f,g,h,i,j
max = max(value)
if max==0:
    print('There are no Odd numbers.')
else:
    print(max,"Is the largest Odd integers")
