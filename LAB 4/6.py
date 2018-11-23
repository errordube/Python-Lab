def max_of_three(a,b,c):
 
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
 
print ("Function to find the largest of three numbers")
 
print ("Enter the first  number")
firstNumber = int(input()) 
 
print ("Enter the second  number")
secondNumber = int(input())
     
print ("Enter the third  number")
thirdNumber = int(input())
 
print ("Largest of " +str(firstNumber) +", " +str(secondNumber) +", " +str(thirdNumber) +" is " +str(max_of_three(firstNumber,secondNumber,thirdNumber)))
