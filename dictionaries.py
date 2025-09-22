# Dictionary to store user information in key-value pairs

monthConversions = { "Jan": "January", 
                        "Feb": "February",
                        "Mar": "March",
                        "Apr": "April",
                        "May": "May",
                        "Jun": "June",
                        "Jul": "July",
                        "Aug": "August",
                        "Sep": "September",
                        "Oct": "October",    #using a dictionary to map short month names to full month names
                        "Nov": "November",   #Cannot have duplicate keys in a dictionary, if you do the last one will overwrite the previous one
                        "Dec": "December", } # key is the short form of the month, value is the full name of the month
print(monthConversions["Jan"]) #accessing value in dictionary using key
print(monthConversions.get("Luv")) #another way to access value in dictionary using key, more advanced
print(monthConversions.get("Luv","Not a valid key")) #if key does not exist, return default value instead of error
print(monthConversions) #print the whole dictionary

#Dictionaries can store different data types as values, including integer, float, boolean, list, another dictionary, etc.