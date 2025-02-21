import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

mod_numbers=[] #Create a list for the modified numbers
for n in random_numbers:
    if n>50: #Checks if element n in random_numbers is bigger than 50
        mod_numbers.append(random.randint(20,30)) #If it is it changes the list mod_numbers with a random integer from the range 20-30
    else:
        mod_numbers.append("xx") #If it is not (meaning n<50) it replaces the elements in the list with xx
print(mod_numbers) #Prints the list
