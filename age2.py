"""
Title: Age Problem Version 2: Frodo and Gollum - Lab 2 Demo
This program asks the user to make a character with a certain age, and it compares that age to Frodo's age and Gollum's age.
Author: Sami Pokharel
Date: September 28, 2023
"""
# Input of character descriptions
character_name = input("Enter the character's name: ")
character_age = int(input("Enter the character's age: "))
# Variables for the ages of Frodo and Gollum - Hard coded variables
frodo_age = 51
gollum_age = 589
# Compound statements and Output
if character_age < frodo_age:  # If the character_age is smaller than Frodo's age who has the smallest age, then they are considered to be younger. 
    print(f"{character_name} is {character_age} years old, and they are younger than Frodo and Gollum")
elif character_age > gollum_age:  # If the character_age is larger than Gollum's age who has the largest age, then they are considered to be older. 
    print(f"{character_name} is {character_age} years old, and they are older than Frodo and Gollum")
else:
    print(f"{character_name} is {character_age} years old, and they are older than Frodo but younger than Gollum")