from studentrecord import d1,d2,d3,d4,d5,d6
print "students with same Service providers are:"
print "-----------BSNL users--------------"
for i,j in d3.iteritems():
    if (j.find("94")==0):
        print d1[i],d2[i],d3[i],d4[i],d5[i],d6[i]
print "-----------Airtel users------------"
for i,j in d3.iteritems():
    if (j.find("98")==0):
        print d1[i],d2[i],d3[i],d4[i],d5[i],d6[i]
print "-----------Idea users------------"
for i,j in d3.iteritems():
    if (j.find("89")==0 or j.find("97")==0):
        print d1[i],d2[i],d3[i],d4[i],d5[i],d6[i]
print "-----------Reliance users------------"
for i,j in d3.iteritems():
    if (j.find("77")==0):
        print d1[i],d2[i],d3[i],d4[i],d5[i],d6[i]
print "-----------Vodafone users------------"
for i,j in d3.iteritems():
    if (j.find("99")==0):
        print d1[i],d2[i],d3[i],d4[i],d5[i],d6[i]
print "-----------Docomo users------------"
for i,j in d3.iteritems():
    if (j.find("79")==0):
        print d1[i],d2[i],d3[i],d4[i],d5[i],d6[i]
