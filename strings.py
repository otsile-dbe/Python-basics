print("Palesa's\nWorld") #escape sequence for new line 
print("Palesa's\"World\"") #escape sequence for double quote

phrase = "Palesa's World"
print(phrase) #printing the string variable
print(phrase.lower()) #lowercase
print(phrase.upper()) #uppercase
print(phrase.isupper()) #check if all characters are uppercase
print(phrase.upper().isupper()) #check if all characters are uppercase after converting to uppercase
print(phrase + " is awesome") #string concatenation
print(len(phrase)) #length of the string
print(phrase[0]) #indexing to get first character
print(phrase[0:5]) #slicing to get first 5 characters
print(phrase.index("W")) #index of character W to find its position
print(phrase.replace("World", "Universe")) #replacing World with Universe

