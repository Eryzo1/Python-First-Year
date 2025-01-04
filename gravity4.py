'''
Title: Lab 4 Demo Version 4: - Combining several cipher methods!
This program uses functions to efficiently print out whatever output is deccrypted from the several ciphers, and uses function composition to get many different results.
Author: Sami Pokharel
Date: October 10, 2023
'''
# Import String Module
import string
# Using the string Module to store all of the letters of the alphabet in a variable
capital_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase

def decrypt_caesar(text: str, shift: int) -> str:
    """
    This function has 2 parameters, text and shift, where whatever index values inside of text are shifted based on the number assigned to the shift parameter.
    Returns a string
    """
    letters_list = []
    # For loop to loop through the text which is the input 
    for index in range(len(text)):
        if text[index] in capital_letters:
            find_input_index = capital_letters.find(text[index])
            letters_list.append(capital_letters[find_input_index - shift%len(capital_letters)])  # Loops through capital_letters so that when shifted by a number larger than the list, it will not output an error.
            output = "".join(letters_list)
        elif text[index] in lowercase_letters:
            find_input_index = lowercase_letters.find(text[index])
            letters_list.append(lowercase_letters[find_input_index - shift%len(lowercase_letters)])  # Loops through capital_letters so that when shifted by a number larger than the list, it will not output an error.
            output = "".join(letters_list)
        else:
            letters_list.append(text[index])
            output = "".join(letters_list)
    # Output value of the function
    return output    

def decrypt_atbash(text: str) -> str:
    """
    This function has only 1 parameter which is text. This function's purpose is to find the index values of text and output the reverse value of the original index value of text.
    Returns a string
    """
    letters_list = []
    # For loop to loop through the text which is the input
    for index in range(len(text)):
        if text[index] in capital_letters:
            find_input_index = capital_letters.find(text[index])
            letters_list.append(capital_letters[-find_input_index - 1])  # We subtract 1 because when we do the -index value inside of capital_letters, it does not start at 0 but -1.
            output = "".join(letters_list)
        elif text[index] in lowercase_letters:
            find_input_index = lowercase_letters.find(text[index])
            letters_list.append(lowercase_letters[-find_input_index - 1])  # We subtract 1 because when we do the -index value inside of lowercase_letters, it does not start at 0 but -1.
            output = "".join(letters_list)
        else:
            letters_list.append(text[index])
            output = "".join(letters_list)
    # Output value of the function
    return output

def decrypt_a1z26(text: str) -> str:
    """
    This function has only 1 parameter which is text. This function's purpose is to replace the inputed numbers in text with one of the letters of the alphabet at the inputed number position.
    It also replaces the dashes when the user inputs the number and dashes in a certain order for an empty string so that all of the letters are joined together when outputted. 
    Returns a string
    """
    # For loop to loop through the letters of the alphabet in inverse order. 26 - 1
    for i in range(len(capital_letters), 0, -1):
        text = text.replace(str(i), capital_letters[i - 1])
    text = text.replace("-", "")
    # Output value of the function
    return text
def main() -> None:
    """
    Main program. This function is only used to print other functions for efficiency. Once called it will output all print statements. 
    """
    # Input
    text = input("Enter a text to decipher: ")
    # Output
    print("Let's try all the methods we have:")
    output_caesar = decrypt_caesar(text, 3)
    output_atbash = decrypt_atbash(text)
    output_a1z26 = decrypt_a1z26(text)
    print(f"Caesar cipher: {output_caesar}\nAtbash cipher: {output_atbash}")
    print(f"Combined: 1) Caesar; Atbash cipher: {decrypt_atbash(output_caesar)}")
    print(f"Combined: 1) Atbash; Caesar cipher: {decrypt_caesar(output_atbash, 3)}")
    print(f"A1Z26 cipher: {output_a1z26}")
    print(f"Combined: 1) A1Z26; 2) Caesar cipher: {decrypt_caesar(output_a1z26, 3)}")
    print(f"Combined: 1) A1Z26; 2) Atbash cipher: {decrypt_atbash(output_a1z26)}")
    print(f"Comnined: 1) A1Z26; 2) Atbash; 3) Caesar cipher: {decrypt_caesar(decrypt_atbash(output_a1z26), 3)}")
    print(f"Combined: 1) A1Z26; 2) Caesar; 3) Atbash cipher: {decrypt_atbash(decrypt_caesar(output_a1z26, 3))}")
# Calling the main function
main()



