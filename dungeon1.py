MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    matrix = []
    file = open(map_file, "r")
    text = file.read()
    text = text.splitlines()
    for line in text:
        a_row = []
        for j in range(len(line)):
            a_row.append(line[j])
        matrix.append(a_row)
    return matrix

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "S":
                return [i, j]

def get_command() -> str:
    """
    Gets a command from the user.
    """
    user_input = input().lower()
    return user_input

def main():
    """
    Main entry point for the game.
    """
    map_file = load_map(MAP_FILE)
    print(map_file)
    starting_position = find_start(map_file)
    print(starting_position)
    while True:
        user_input = get_command()
        if user_input == "escape":
            break
        else:
            print("I do not understand.")

if __name__ == '__main__':
    main()
