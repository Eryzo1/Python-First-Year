"""
Tempertature lab - Lab 1 demo
This program takes temperature in celsius and changes it to fahrenheit.
Author: Sami Pokharel
Date: September 19, 2023
"""
# Input
temp_c = int(input("What is the current temperature in Canada? ")) 
# Using the round function to round the number to the nearest whole number
temp_f = round((temp_c * 9 / 5) + 32)  # This formula is to convert temperature from celsius to fahrenheit
# Output
print(f"{temp_c} degress in Canada would be {temp_f} degrees in Springfield. D'oh!")