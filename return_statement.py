#Using return statements in functions

def cube(number): # function has one paramter, named number
    return number * number * number # returns the cube of the number, as you gave it instruction to return number multiplied by itself twice, 
print(cube(3)) # prints 27
# note after the return statement, the function ends and no further code in the function (indented body) can be executed

#You can store the return value of a function in a variable
result = cube(4) # result variable now holds the return value of cube(4)
print(result) # prints 64, notice this variable does not need quotation marks.