# Opening a file
filename = "C:/Users/SamiP/Desktop/Coding/Lab 3 Demo/klingon-english.txt"
filemode = "r"
with open(filename, filemode, encoding="utf-8") as file:
    text = file.readlines()
# Changes to the file
removed_whitespace_line3 = text[2].strip()  # Variable for the white spaces removed for the 3rd line.
verticalbar_index = removed_whitespace_line3.find("|")  # Variable to find the index of the vertical bar.
# Input
question = input(f"How do you translate {removed_whitespace_line3[verticalbar_index + 1:]} to Klingon?\n")
# Output
if question == removed_whitespace_line3[:verticalbar_index]:
    print("Correct!")
else:
    print(f"Sorry, you're wrong!")
    print(f"The correct answer is {removed_whitespace_line3[:verticalbar_index]}")