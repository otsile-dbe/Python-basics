# Making Pig Latin Translator with function operator/command

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #checking if letter we want to loop is in the string defined, use lower operator to account for all vowels upper and lowercase
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation 
print(translate(input("Enter a phrase: ")))

    