#Example 1 of for loops 

for letter in "Education": #Creating a for loop that iterates through each letter in the string "Education"
    print(letter) #Printing each letter on a new line, we can define a vairable called letter to represent each character in the string as we loop through it
    
    
#Example 2 of for loops
for item in ["apple", "banana", "cherry"]: #Creating a for loop that iterates through each item in the list of fruits
    print(item) #Printing each item on a new line, we can define a variable called item to represent each element in the list as we loop through it
    #Note that the variable name (ie the word item and letter in the code) can be anything, it does not have to be item, it can be fruit, or anything else that makes sense to you


#Example 3 of for loops with range function
for index in range(5): #Creating a for loop that iterates through a sequence of numbers from 0 to 4 (5 is exclusive)
    print(index) #Printing each number on a new line, we can define a variable called index to represent each number in the range as we loop through it
    #Note that the range function can take two arguments, the start and end of the range, so range(1, 6) would give us numbers from 1 to 5

friends = ["Alice", "Bob", "Charlie"] #Creating a list of friends
for friend in friends: #Creating a for loop that iterates through each friend in the list
    print("Hello " + friend) #Printing a greeting for each friend, using the variable friend to represent each element in the list as we loop through it
    
friends = ["Alice", "Bob", "Charlie"]
for index in range(len(friends)): #Creating a for loop that iterates through the indices of the list using the range function and len function
    print("Hello " + friends[index]) #Printing a greeting for each friend, using the index variable to access each element in the list by its index

#Example 4 of for loops with range function and if statements inside the loop
for i in range(10): #Creating a for loop that iterates through a sequence of numbers from 0 to 9
    if i % 2 == 0: #Checking if the number is even
        print(i) #Printing the even number
#With for loops we can loop with an array, a string, or a range of numbers, and we can also use if, elif, and else statements inside the loop to perform different actions based on conditions

#Example 5 of nested for loops
for i in range(3): #Outer loop that iterates through numbers 0 to 2
    for j in range(2): #Inner loop that iterates through numbers 0 to 1
        print(f"i: {i}, j: {j}") #Printing the values of i and j for each iteration of the inner loop
        