from studentrecord import d1,d2,d3,d4,d5,d6
a=input("enter host name:")
print "students with same host are:"
for i,j in d6.iteritems():
    if a in j:
        print d1[i],d2[i],d3[i],d4[i],d5[i],d6[i]
            
