"""
Title: Chalkboard Problem - Lab 1 Demo
This is a simple input and output program where the user enters a phrase and the # of times to repeat that phrase and the output will be that phrase repeated a number of times. 
Author: Sami Pokharel
Date: September 19, 2023
"""
# Input 
phrase = input("What is the phrase? ")
repeat = int(input("How many times do you want to write it? "))  # The int function allows it so that when multiplying the phrase variable and repeat variable it does not output an error
# Output
print((phrase + " ") * repeat)