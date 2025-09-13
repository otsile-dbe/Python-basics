friends = ["Mommy", "Nala", "Asanda", "Khono", "Zuki", "Tokollo"] #use square brackets for lists
friends[2] = "Babe" #replace item in list
print(friends[0]) #prints first item in list
print(friends[0:3]) #prints first 3 items in list
print(friends[-1]) #prints last item in list


ages = [5, 10, 15, 20, 25] #variable can hold different data types
friends = ["Mommy", "Nala", "Asanda", "Khono", "Zuki", "Tokollo"] #use square brackets for lists
friends.extend(ages) #adds ages list to friends list
print(friends)


friends = ["Mommy", "Nala", "Asanda", "Khono", "Zuki", "Tokollo"] #use square brackets for lists
friends.append("Babe") #adds item to end of list
print(friends)


friends = ["Mommy", "Nala", "Asanda", "Khono", "Zuki", "Tokollo"] 
friends.insert(3, "Violet") #inserts item at index 3
friends.remove("Khono") #removes item from list
print(friends)


friends = ["Mommy", "Nala", "Asanda", "Khono", "Zuki", "Tokollo"] 
friends.clear() #removes all items from list
print(friends)

friends = ["Mommy", "Nala", "Asanda", "Asanda", "Khono", "Zuki", "Asanda", "Tokollo"]
friends.sort() #sorts list in alphabetical order
print(friends)
friends.reverse() #reverses order of list
print(friends)
print(friends.index("Asanda")) #prints index of item in list
print(friends.count("Asanda")) #prints number of times item appears in list

friends2 = friends.copy() #copies list to new variable
print(friends2)