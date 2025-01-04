"""
Title: Episode name problem - Lab 1 demo
This program uses string slicing to convert the initial format of the input to a new format and output the data in that new format.  
Author: Sami Pokharel
Date: September 19, 2023
"""
# Input
epi_name = input("What is the name of the episode? ")
# Using the find function to find the index positions of the letter E, first underscore and second underscore.   
e_letter_position = epi_name.find("E")
uscore1_index = epi_name.find("_")
uscore2_index = epi_name.find("_", e_letter_position)
# Using string slicing to extract the season, episode and name. 
season = epi_name[1:uscore1_index]
episode = epi_name[e_letter_position + 1:uscore2_index]  # Using +1 so the index position starts after the initial position. 
name = epi_name[uscore2_index + 1:]  # Using +1 so the index position starts after the initial position.
# Output
print(f"Season {season}, Episode {episode}: {name} (The Simpsons)")


