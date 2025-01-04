import random

def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    with open(filename, "r") as file:
        text = file.read()
        spells_list = text.splitlines()

    return spells_list

def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    random_spell = random.choice(spells).lower()

    return random_spell

def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    print("############################################################")
    print("Harry Potter Typing Trainer")
    print("############################################################")

def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    with open("instructions.txt", "r") as file:
        text = file.read()
    return text

def get_user_input(spell: str) -> str:
    """
    Gets the spell as input from the user and returns it.
    """
    user_input = input(f"Type the following spell: {spell}\n").lower()
    return user_input

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    if spell == user_input:
        # print("Correct")
        return True
    else:
        # print(f"Incorrect\nThe spell was: {spell}")
        return False

def play_again() -> bool:
    """

    """
    user_input = input("Do you want to practice more? (y/n)\n").lower()
    if user_input == "y":
        return False
    else:
        return True

def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    display_header()
    print(display_instructions())
    score = 0
    while True:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        if display_feedback(spell, user_input):
            score += 10
            print("Correct")
            print(f"You get {score} points! Your score is: {score}")
        else:
            score -= 5
            print(f"Incorrect\nThe spell was: {spell}")
            print(f"You lose! Your score is: {score}")
        
        if play_again():
            print(f"Your final score is: {score}")
            break
        
main()