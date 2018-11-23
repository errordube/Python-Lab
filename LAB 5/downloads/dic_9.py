from studentrecord import d1,d2,d3,d4,d5,d6
a=d4.values()
print "students with same STATE are:"
for i,j in d4.iteritems():
    if(a.count(j)>1):
        print d1[i],d2[i],d3[i],d4[i],d5[i],d6[i]
