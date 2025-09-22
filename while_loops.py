#While loops execute a set of statements as long as a condition is true.

i = 1 #initialize variable
while i <= 30: #set condition for while loop
    print(i) #print the variable
    i += 1 #increment the variable to eventually break the loop
print("Done with loop") #print when loop is done


#More complex example of while loop, with if, elif, else statements inside the loop

i = 1 
while i <= 30: 
    print(i) 
    i += 1 
    if i == 10: #if statement inside while loop
        print("You reached 10!") 
    elif i == 20: #elif statement inside while loop
        print("You reached 20!")
    else: #else statement inside while loop
        print("Not 10 or 20 yet")
print("Done with loop")