num1 = (input("Enter first number: ")) 
num2 = (input("Enter second number: "))
result = int(num1) + int(num2) #type conversion from string to integer so we can add
print("The sum is: " + str(result)) #only works for integer addition

num3 = (input("Enter first number: ")) 
num4 = (input("Enter second number: "))
result = float(num3) + float(num4) #type conversion from string to float so we can add decimal numbers
print("The sum is: " + str(result)) #works for both integer and decimal addition
