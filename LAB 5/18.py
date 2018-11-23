import math
odd={}
i=1
while i<50:
    odd.update({i:math.log(i,2)})
    i+=2
print odd
