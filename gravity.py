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

def main() -> None:
    """
    Main program.
    This function is only used to print other functions for efficiency. Once called it will output all print statements. 
    """
    # Input
    text = input("Enter a text to decipher: ")
    # Calling the function and assigning it to a variable to output the results.
    output = decrypt_caesar(text, 3)
    print(output)

main()

