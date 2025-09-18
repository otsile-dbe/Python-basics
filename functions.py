def say_goodbye(): #create a function with def keyword, everything indented after def is part of the function
    print("Goodbye! Thanks for coding!") #function body, indented code that only runs when function is called
    
say_goodbye() #call the function to run all the code of instructions indented inside it

    
print("Top")
say_goodbye() #function can be called anywhere in the code after it is defined, even in between other code like strings
print("Bottom")

#Functions with parameters
def say_hello(name): #name is a parameter, parameters are variables that are passed to the function when it is called
   print("Hello Palesa") 
   
say_hello("Palesa") #Palesa is an argument, argument is the value passed to the function when it is called

def say_hello(name): #name is a parameter
   print("Hello " + name)
   
say_hello("Otsile") #Otsile is an argument, argument is the value passed to the function when it is called
say_hello("John") #can call function with different arguments

#Functions with multiple parameters
def come_back(name,age,place): #multiple parameters separated by commas
    print("Come back! " + name + "! You are only " + age + " years old and cannot go to " + place + " alone!") #function body
    
come_back("Palesa","15","the club") #call function with multiple arguments
come_back("Otsile","10","the mall") #can call function with different arguments