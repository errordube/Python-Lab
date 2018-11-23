from studentrecord import d1,d2,d3,d4,d5,d6
print "details of student who have the highest average marks among all:"
mx=0
for i,j in d5.iteritems():
    avg=(j[0]+j[1]+j[2])/3
    if avg>mx:
        mx=avg
        h=i
        
print d1[h],d2[h],d3[h],d4[h],d5[h],d6[h],"avg =",mx
            
