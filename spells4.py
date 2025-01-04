"""
Title: Lab 5 Demo - Harry Potter Typing Trainer Version 4
This program times how fast the user can type a randomly outputted spell from Harry Potter and they get a certain amount of points based on how fast they can type.
Author: Sami Pokharel
Date: October 20, 2023
"""
# Import time and random libraries
import time
import random

def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    # Opening files and reading the file
    with open(filename, "r") as file:
        text = file.read()
        spells_list = text.splitlines()  # Getting rid of all the newlines and putting the spells into a list. 

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
    # Opening files and reading the file
    with open("instructions.txt", "r") as file:
        text = file.read()
    return text

def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    if spell == user_input:
        return True
    else:
        return False

def play_again() -> bool:
    """
    Asks the user to input if they want to play again or not.
    """
    user_input = input("Do you want to practice more? (y/n)\n").lower()
    if user_input == "y":
        return False
    else:
        return True
    
def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """
    target_time = len(spell) * 0.3
    return round(target_time, 1)

def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    """
    points = 0
    target_time = get_target_time(spell)
    if display_feedback(spell, user_input):
        if user_time <= target_time:
            points = 10
        elif user_time <= (target_time * 1.5) and user_time > target_time:
            points = 6
        elif user_time <= (target_time * 2) and user_time > (target_time * 1.5):
            points = 3
        elif user_time > (target_time * 2):
            points =  1
    else:
        points = -5
    
    return points

def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    display_header()
    print(display_instructions())
    score = 0
    # While loop to continue looping till the player inputs n
    while True:
        spell = get_random_spell(spells)
        user_input, user_time = get_user_input(spell)
        points = calculate_points(spell, user_input, user_time)
        score += points
        if display_feedback(spell, user_input):
            print("Correct")
            print(f"You get {points} points! Your score is: {score}")
        else:
            print(f"Incorrect\nThe spell was: {spell}")
            print(f"You get {points} points! Your score is: {score}")
        if play_again():
            print(f"Your final score is: {score}")
            break
# Calling the main function. 
main()
