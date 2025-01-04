filename = "C:/Users/SamiP/Desktop/Coding/Lab 3 Demo/klingon-english.txt"
filemode = "r"
with open(filename, filemode, encoding="utf-8") as file:
    text = file.readlines()

klingon_consonants = ["b", "ch", "D", "gh", "H", "j","l","m", "n", "p", "q","Q", "r", "S","t","v","w","y", "'"]
new_list = []
klingon_words = []
english_words = []
for line in range(len(text)):
    removed_whitespace_file = text[line].strip()
    new_list.append(removed_whitespace_file.split('|'))

for i in range(len(new_list)):
    klingon_words.append(new_list[i][0])
    english_words.append(new_list[i][1])

consonants_input = input("What consonant do you want to practice with?\n")
x = True
while x:
    if consonants_input in klingon_consonants:
        index = klingon_consonants.index(consonants_input)
        question = input(f"How do you translate {english_words[index]} to Klingon?\n")
        if question == klingon_words[index]:
            print("Correct")
            x = False
        else:
            attempts = 3
            while attempts > 0:
                print("Sorry, you're wrong!")
                print(f"How do you translate {english_words[index]} to Klingon? You have {attempts} attempts left.")
                first_letter = klingon_words[index][0]
                last_letter = klingon_words[-1]
                middle_letter = "*" * (len(new_list[i][0]) - 2) 
                print(f"Hint:{first_letter}{middle_letter}{last_letter}")
                question = input()
                attempts -= 1
                if attempts == 0:
                    print("Sorry, you're wrong!")
                    print(f"The correct answer is {klingon_words[index]}.")
                    x = False
    if consonants_input not in klingon_consonants:
        pass