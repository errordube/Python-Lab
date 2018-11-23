from studentrecord import d1,d2,d3,d4,d5,d6
a=d2.values()
print("Students with same hometown are: ")
for i,j in d2.iteritems():
    if(a.count(j)>1):
        print("d1[i],d2[i],d3[i],d4[i],d5[i],d6[i]")
