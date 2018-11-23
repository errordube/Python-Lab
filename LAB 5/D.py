a=[]
n=input("Enter the number of elements in list:")
for x in range(0,n):
    element=input("Enter element: ")
    a.append(element)
b=a[::-1]
print("New list is:")
print(b)
