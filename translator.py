# Making Pig Latin Translator with function operator/command

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": #checking if letter we want to loop is in the string defined
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation 

print(translate("Bok"))
print(translate(input("Enter a phrase:")))

    