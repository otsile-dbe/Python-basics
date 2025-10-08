class Student:  #Class for the template of a student with empty data sets
    
    def __init__(self, name, major, APS, is_on_probation):  #initialize used to map out what attributes a student should have for this class
        self.name = name 
        self.major = major
        self.APS = APS 
        self.is_on_probation = is_on_probation
        
    def on_honour_roll(self): #putting functions inside of a class
     if self.APS >= 40:
        return True 
     else:
        return False 
        