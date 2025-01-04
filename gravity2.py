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

def main() -> None:
    """
    Main program.
    """
    text = input("Enter a text to decipher: ")
    print("Let's try all the methods we have:")
    output_caesar = decrypt_caesar(text, 3)
    output_atbash = decrypt_atbash(text)
    print(f"Caesar cipher: {output_caesar}\nAtbash cipher: {output_atbash}")

main()

