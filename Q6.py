#A list being mutable means that it can be altered while a string (which is immutable) cannot.
#Producing a change in a list will return a changed list, for example:
list=[1,2,3,4] #This is our original list
#We can produce a series of changes:
list.append(5) #We add an element to the list
list2=["a","b","c"]
list.extend(list2) #We add a second list to the first
list.remove(3) #We remove number 3 from the list
del list[1:2] #We delete the elements in certain position

print(list) #When printing the original list, it has all the changes we have produced

#On a string this is different:
string="today is friday 21st of February"
string.replace("21st", "22nd") #Replaces a character in the string with another
string.capitalize() #Capitalizes the string

print(string) #Unlike the list, printing the original string does not show the changes made to it. This is why strings are immutable and lists are not

