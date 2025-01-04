"""
Title: Age Problem Version 1: Frodo - Lab 2 Demo
This program asks the user to make a character with a certain age, and it compares that age to Frodo's age. 
Author: Sami Pokharel
Date: September 28, 2023
"""
# Input of character descriptions
character_name = input("Enter the character's name: ")
character_age = int(input("Enter the character's age: "))
# Variable for the age of Frodo - Hard coded variable
frodo_age = 51
# Compound statements and Output
# If the age is smaller, older, or the same as Frodo, it outputs a comparison of the character to Frodo. 
if character_age > frodo_age:
    print(f"{character_name} is {character_age} years old, and they are older than Frodo.")
elif character_age < frodo_age:
    print(f"{character_name} is {character_age} years old, and they are younger than Frodo.")
else:
    print(f"{character_name} is {character_age} years old, and they are the same age as Frodo.")