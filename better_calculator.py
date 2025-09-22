#Better calculator with advanced operations

num1 = float(input("Enter first number: ")) #convert input so you can do both integer and decimal addition, and not just string concatenation
op = input("Enter operator:") #get the operator from the user
num2 = float(input("Enter second number: "))
if op == "+":
    print(num1 + num2) #using if statements to check for operator and do the corresponding operation
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
