#Examples of chef class file 

from chef_class import Chef

myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

from chef_class import ChineseChef 

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_chicken()

#Using inheritance to get data from chef_class

class AfricanChef(ChineseChef): #Inherits all data from ChineseChef class so you do not have to copy and paste to redefine it 
    def make_chicken(self):
        return super().make_chicken()
    
myAfricanChef = AfricanChef()
myAfricanChef.make_chicken()
myAfricanChef.make_fried_rice()
    
