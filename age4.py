"""
Title: Age Problem Version 4: Fellowship of the Ring
This program asks the user to make a character with a certain age, and it compares that age to the ages inside of a list.
Author: Sami Pokharel
Date: September 28, 2023
"""
# Input of character descriptions
character_name = input("Enter the characters name: ")
character_age = int(input("Enter the characters age: "))
# A parallel list of all the names of every character and their ages
names = [
    "Frodo",
    "Samwise",
    "Gandalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]
# Empty lists for appending the names that are older and younger than the character.
names_older = []
names_younger = []
# Variable to seperate the characters in the list by a comma. 
seperator = ", "
# A loop that compares the character_age to the numbers inside the ages list. 
for index in range(len(names)):  # The length of the names list is the same as the length of the ages list, and the index values are parallel. 
    if character_age < ages[index] and character_age > 0:  # Character_age is greater than 0 so that it does not include negative numbers. 
        names_older.append(names[index])
    elif character_age > ages[index]:
        names_younger.append(names[index])
# Output 
if len(names_younger) > 0:  # If there is nothing inside of the list then it will not print anything. 
    print(f"{character_name} is {character_age} years old, and they are older than {seperator.join(names_younger)}")
if len(names_older) > 0:  # If there is nothing inside of the list then it will not print anything.
    print(f"{character_name} is {character_age} years old, and they are younger than {seperator.join(names_older)}")
if character_age < 0:  
    print("Invalid age")
