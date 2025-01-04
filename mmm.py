"""
Title: Mmm... - Lab 1 Demo
This is a simple input and output program where the user is asked to enter information and it outputs that information in a certain way. 
Author: Sami Pokharel
Date: September 19, 2023
"""
# Input
user_data = input("What is the tasty thing? ").lower()  # The .lower function is used so that the output will always be lowercase no matter what the user enters
# Output
print(f"Mmm... {user_data}")