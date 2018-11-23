a=input("Enter any String: ")
for i in range(len(a)):
    c=a.count(a[i])
    if c==1:
        print(a[i])
        break
