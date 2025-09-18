coordinates = (15,30) #create a tuple using parentheses, tuple is a lot like a list but tuples are immutable meaning you cannot change them once created 
print(coordinates[0]) #prints first item in tuple

#Difference between tuples and lists
#Tuples are immutable meaning you cannot change them once created
#Lists are mutable meaning you can change them once created
#Tuples use parentheses ()
#Lists use square brackets []
#Tuples are used for fixed data that should not be changed
#Lists are used for data that can change

coordinates = [(15,30), (20,25), (50,60)] #list of tuples
print(coordinates[0]) #prints first tuple in list, the list is mutable but the tuples inside it are immutable

