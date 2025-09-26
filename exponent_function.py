#Using for loops to create an exponent function

def exponent_function(base_num, exp_num): #Defining a function that takes two parameters, base and exp
    result = 1 #Initialize result variable to 1
    for index in range(exp_num): #For loop that loops through range of exp_num
        result = result * base_num #Multiply result by base_num in each iteration, defining exponentiation as repeated multiplication
    return result #Return the final result after the loop, review how return statements work in functions

print(exponent_function(2, 3)) #Calling the function with base 2 and exponent 3, should return 8 (2*2*2), note that you can also do this with input commands to get user input
print(exponent_function(3, 4)) #Calling the function with base 3 and exponent 4, should return 81 (3*3*3*3)

#Example of using the function with user input

base = int(input("Enter base number: ")) #Get base number from user input, convert to integer
exp = int(input("Enter exponent number: ")) #Get exponent number from user input, convert to integer
print(exponent_function(base, exp)) #Call the function with user-provided base, since you have already defined the function, you can call it as many times as you want with different inputs
