def prime(mn,mx):
    a=[]
    while mn<=mx:
        c=0
        i=1
        n=mn
        while(i<=n/2):
            if(n%i==0):
                c+=1
            i+=1
        if(c==1):
            a.append(mn)
        mn+=1
    return a
a=prime(50,100)
print a
d={}
for j in a:
    d.update({j:(j%10)+(j/10)})
print d
