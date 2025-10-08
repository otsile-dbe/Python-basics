#Classes and objects used to organize your data and code 
#Class command used to create your own data type and later use in your code 


#Example 1, Using class variable to make object

from student_class import Student #Importing the class student from the file student_class we created for this purpose 

student1= Student("Palesa", "Physics", 41, True) #Now it is a student object with actaul data that we created from the class variable
student2= Student("Khono", "IT", 37, False)

print(student1.name)
print(student1.APS)
print(student2.major)


        
    

