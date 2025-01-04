# Opening a file
filename = "C:/Users/SamiP/Desktop/Coding/Lab 3 Demo/klingon-english.txt"
filemode = "r"
with open(filename, filemode, encoding="utf-8") as file:
    text = file.readlines()
# Lists 
klingon_consonants = ["b", "ch", "D", "gh", "H", "j","l","m", "n", "p", "q","Q", "r", "S","t","v","w","y", "'"]
new_list = []
# Changes in the file
for line in range(len(text)):
    removed_whitespace_file = text[line].strip()
    new_list.append(removed_whitespace_file.split('|'))
# Input
consonant_input = input("What consonant do you want to practice with?\n")
x = True
while x:
    for i in range(len(new_list)):
        if consonant_input == klingon_consonants[i]:
            question = input(f"How do you translate {new_list[i][1]} to Klingon?\n")
            if question == new_list[i][0]:
                print("Correct!")
                x = False
            else:
                    print(f"Sorry, you're wrong!")
                    print(f"The correct answer is {new_list[i][0]}")
                    x = False
        elif consonant_input not in klingon_consonants:
            consonant_input = input("Please enter a valid Klingon consonant.\n")
            for i in range(len(new_list)):
                if consonant_input == klingon_consonants[i]:
                    question = input(f"How do you translate {new_list[i][1]} to Klingon?\n")
                    if question == new_list[i][0]:
                        print("Correct!")
                        x = False
                    else:
                        print(f"Sorry, you're wrong!")
                        print(f"The correct answer is {new_list[i][0]}")
                        x = False
