#If statements respond and execute code when conditions given are met

#Example 1: one condition

tired = True #boolean variable, can only be True or False
if tired: #if statement checks if condition is True
    print("I sleep") #if condition is True, this line executes



#Example 2: if-else statement, two conditions
raining = False #condition of if statement
if raining:
    print("I take an umbrella")
else:
    print("I wear shorts")
#any string outside the indented if statement will not run with the if statement
  
  
    
#Example 3

is_female = True
is_tall = True
 
if is_female or is_tall: #if either condition is True, this block executes
     print("You are female, or tall, or both")
else:
    print("You are neither")
if is_female and is_tall: #if both conditions are True, this block executes
    print("You are a tall woman")
    
#Condition using elif and not  
is_strong = False
is_fast = True
if is_strong and is_fast: #if both conditions are True, this block executes
    print("You are a strong and fast person")
elif is_strong and not(is_fast): #elif means else if, checks another condition if the first is False
    print("You are strong but not fast")
elif not(is_strong) and is_fast:
    print("You are not strong, but you are fast")
else:
    print("You are neither strong nor fast")



    
    




