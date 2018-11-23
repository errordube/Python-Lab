from studentrecord import d1,d2,d3,d4,d5,d6
print "details of student who scored highest marks in chemistry:"
mx=0
for i,j in d5.iteritems():
    if j[1]>mx:
        mx=j[1]
        h=i
        
print d1[h],d2[h],d3[h],d4[h],d5[h],d6[h]
            
