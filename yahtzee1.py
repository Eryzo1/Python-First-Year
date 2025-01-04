'''
Title: Yahtzee Version 1 Code: Upper Section - Lab 6 Demo
This program is a game of Yahtzee
Author: Sami Pokharel
Date: November 3, 2023
'''
# Import random module library
import random

def make_roll() -> tuple:
    """
    Returns a tuple of five random values between 1 and 6.
    """
    # Turns the tuple into a list because lists are mutable
    my_tuple = (0,) * 5  # This tuple can have anything inside of it because we are changing the value when we convert it into a list.
    converted_tuple = list(my_tuple)
    for i in range(len(my_tuple)):
        converted_tuple[i] = random.randint(1,6)  # All the values inside the converted tuple are now a random number between 1-6
    my_tuple = tuple(converted_tuple)
    print(f"Rolling the dice... {my_tuple}")
    return my_tuple

def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    Example: sum_of_given_number((2,6,2,6,1), 6) = 12
    """
    # Appending the values inside of a list so that we can find the sum of all the values that match the number
    my_list = []
    for i in range(len(roll)):
        if roll[i] == number:
            my_list.append(roll[i])
    sum_of_values = sum(my_list)
    return sum_of_values

def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    """
    alist = []
    my_list = [1, 2, 3, 4, 5, 6]
    for i in range(len(my_list)):
        if my_list[i] in roll:
            sum_of_values = sum_of_given_number(roll, my_list[i])
            alist.append(sum_of_values)
        else:
            alist.append(0)
    return alist

def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    for index in range(len(names)):
        print(f"{names[index]}: {upper_section_scores[index]}")

def main():
    """
    Main function.
    """
    atuple = make_roll()
    print("Upper Section:")
    display_upper_section(fill_upper_section(atuple))

if __name__ == "__main__":
    main()

