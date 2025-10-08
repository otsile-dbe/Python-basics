#Using functions inside a class file 

from student_class import Student 

student3 = Student("Retha", "Drama", 39, True ) #The student before the bracket is very important otherwise it becomes a tuple 
print(student3.on_honour_roll())
