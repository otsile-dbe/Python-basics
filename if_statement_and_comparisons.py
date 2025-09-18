#We will do comparions in a function and create a function that will return largest number using if statements

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3: #using comparison operator
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(16,0,86)) #prints our biggest number of function because of how you set comparison and if statements