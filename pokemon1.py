class Pokemon:
    def __init__(self, name, attack, defence, max_health, current_health ) -> None:
        self.name = name
        self.attack = attack
        self.defence = defence
        self.max_health = max_health
        self.current_health = current_health

def main():
    """
    Battle of two Pokemon
    """
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1.name} and {pokemon2.name}!")

if __name__ =='__main__':
    main()