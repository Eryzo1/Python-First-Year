"""
This program takes 2 random pokemon from a file and displays their name and health.
Author: Sami Pokharel
Date: December 8, 2023
"""
import random

class Pokemon:
    '''
    An object in this class represents a single Pokemon
    '''
    def __init__(self, name, attack, defence, max_health, current_health ) -> None:
        """
        Creates and returns a Pokemon object with stats
        """
        self.name = name
        self.attack = attack
        self.defence = defence
        self.max_health = max_health
        self.current_health = current_health
    
    def __str__(self) -> str:
        """ 
        Return a string representation of the Pokemon.
        """
        return f"{self.name} (health: {self.current_health}/{self.max_health})"
    
    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        """
        if amount > 0:
            if amount < self.current_health:
                self.current_health = self.current_health - amount
            elif amount >= self.current_health:
                self.current_health = 0
        
    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        if self.current_health > 0:
            return True
        return False

    def revive(self) -> None:
        """
        Revive the Pokemon.
        """
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")

def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Read a list of Pokemon from a file.
    """
    pokemon_list = []
    file = open(filename, "r", encoding="utf-8")
    next(file) # Continue from the 2nd line instead of the 1st
    for line in file:
        line = line.strip().split("|")
        pokemon_name = line[0]
        pokemon_attack = int(line[1])
        pokemon_defence = int(line[2])
        pokemon_health = int(line[3])
        pokemon_list.append(Pokemon(pokemon_name, pokemon_attack, pokemon_defence, pokemon_health, pokemon_health))
    return pokemon_list

def main():
    """
    Battle of two Pokemon
    """
    pokemon_list = read_pokemon_from_file("all_pokemon.txt")
    pokemon1 = random.choice(pokemon_list)
    pokemon2 = random.choice(pokemon_list)
    while pokemon1 == pokemon2:
        pokemon2 = random.choice(pokemon_list)
    print(f"Welcome, {pokemon1} and {pokemon2}!")

if __name__ =='__main__':
    main()

