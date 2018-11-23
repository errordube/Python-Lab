a=[]
n=input("Enter the number of elements in list: ")
for x in range(0,n):
    element = input("Enter element: ")
    a.append(element)
print(" Maximum element in the list is : ", max(a), "Minimum element in the list is : ", min(a))
