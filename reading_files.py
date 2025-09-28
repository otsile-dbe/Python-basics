#How to read files from another source in python

#Example 1 
employee_file = open("Enter name of file", "enter mode you want to open file in ") #This opens file with specific name under mode you prompt it to, for example read mode allows you to read without changing code of the file 

print(employee_file.readable) #prints files in a readable way, since the file is a string, there is a bunch of commands you can operate on the file

employee_file.close() #This closes the file 

