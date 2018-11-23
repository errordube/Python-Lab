from studentrecord import d1,d2,d3,d4,d5,d6
a=input("enter student's name:")
print "student details :"
for i,j in d1.iteritems():
    if j==a:
        h=i
print d1[h],d2[h],d3[h],d4[h],d5[h],d6[h]
            
