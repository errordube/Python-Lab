def maximum(numOne, numTwo):
    if numOne>numTwo:
        return numOne;
    else:
        return numTwo;

numOne = float(input("Enter your first number, any number:  "))
print("You entered:  {}".format(numOne))
numTwo = float(input("Enter your second number, any number:  "))
print("You entered:  {}".format(numTwo))

print("The larger of the two numbers is: {} ".format(maximum(numOne,numTwo)))
