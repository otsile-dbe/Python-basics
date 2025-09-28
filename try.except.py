#Using a try/except block to allow code to run dispite errors

#Example 1

try: 
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Inavlid input") #Similar to if/else statements, this except command excepts broad conditions, we can specify shown in next example 
    
    
#Example 2

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError: #Catches specific errors, good practice to do this
    print("Divided by zero")
except ValueError:
    print("invalid input")

