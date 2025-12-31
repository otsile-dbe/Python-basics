""" Useful commands for cybersecurity""

#Importing files, open a text file on read mode 
with open("login_attempts.txt", "r") as file:  #using with statement which is like the try statement and accounts for errors so code does not crash
  file_text = file.read()                      #use the read() command to comnvert the file into a readable format for python 
  usernames = file.split()                     #the split() command converts a wjole string text into a list so you can use it that way or read easily
print(file_text)


