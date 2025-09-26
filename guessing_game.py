
#Game with while loops 
#Note before running, note that while loops can store input from users and other variables, and can be used with if, elif, and else statements inside the loop

secret_word = "Coding"
guess = "" #string variable to hold users guess, which we will use in loop condition with input command

while guess != secret_word: #while loop that prompts user to keep guessing until they get the right word
    guess = input("Enter guess: ") #input command to get user input, to be compared to secret word
    
print("You guessed it!") #print when user guesses the correct word



#Guessing game/While loops example with else statements

secret_word = "Python" #before making the loop sett all needed variables
guess = "" 
guess_count = 0 #variable to count number of guesses
guess_limit = 3 #variable to limit number of guesses
out_of_guesses = False #boolean variable to track if user is out of guesses, initially set to false

while guess != secret_word and not(out_of_guesses): #while loop with two conditions, one for correct guess and one for out of guesses
    if guess_count < guess_limit: #if statement to check if user is out of guesses initially
        guess = input("Enter guess: ") 
        guess_count += 1 #increment guess count each time user makes a guess
    else:
        out_of_guesses = True #set out_of_guesses to true if user has reached guess limit
        break #break the loop if user is out of guesses
if out_of_guesses: #else statement to print if user is out of guesses
    print("Out of guesses, you lose!") #print if user is out of guesses
else:
    print("You win!") #print if user guesses the correct word
    