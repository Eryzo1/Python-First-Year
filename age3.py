"""
Title: Age Problem Version 3: Gang of Four - Lab 2 Demo
This program asks the user to make a character with a certain age, and it compares that age to Pippin's age, Frodo's age, Gollum's age, and Arwen's age.
Author: Sami Pokharel
Date: September 28, 2023
"""
# Input of character descriptions
character_name = input("Enter the character's name: ")
character_age = int(input("Enter the character's age: "))
# Variables for the ages of Pippin, Frodo, Gollum and Arwen - Hard coded variables
pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901
# Compound statements and Output
if character_age < 0:  # Age cannot be negative so it has to be greater than 0
    print("Invalid age")
elif character_age < pippin_age:  # If the character_age is smaller than Pippin's age who has the smallest age, then they are considered to be the youngest. 
    print(f"{character_name} is {character_age} years old, and they are younger than Arwen, Gollum, Frodo, Pippin.")
elif character_age < frodo_age:  # Checks for the character_age less than Frodo's age but higher than Pippin's age.
    print(f"{character_name} is {character_age} years old, and they are older than Pippin.")
    print(f"{character_name} is {character_age} years old, and they are younger than Arwen, Gollum, Frodo.")
elif character_age < gollum_age:  # Checks for the character_age less than Gollum's age but higher than Frodo's age and Pippin's age.
    print(f"{character_name} is {character_age} years old, and they are older than Frodo, Pippin.")
    print(f"{character_name} is {character_age} years old, and they are younger than Arwen, Gollum.")
elif character_age < arwen_age:  # Checks for the character_age less than Arwen's age but higher than Gollum's age, Frodo's age, and Pippin's age.
    print(f"{character_name} is {character_age} years old, and they are older than Gollum, Frodo, Pippin")
    print(f"{character_name} is {character_age} years old, and they are younger than Arwen.")
else:
    print(f"{character_name} is {character_age} years old, and they are older than Arwen, Gollum, Frodo, Pippin.")