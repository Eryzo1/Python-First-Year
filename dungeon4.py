"""
This program is a game where the user has to move around a map and reach the finish line, once they reach the finish line then the game ends.
Author: Sami Pokharel
Date: November 24, 2023
"""
# Import Copy library
import copy
# Global Variables
MAP_FILE = 'cave_map.txt'
HELP_FILE = 'help.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    matrix = []
    file = open(map_file, "r")
    text = file.read()
    text = text.splitlines()
    file.close()
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

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    emoji = {" ": "🧱", "S": "🏠", "F": "🏺", "*": "🟢"}
    grid_copy = copy.deepcopy(grid)
    grid_copy[player_position[0]][player_position[1]] = "🧝"
    num_rows = len(grid_copy)
    for row_index in range(num_rows):
        a_row = ''
        num_columns = len(grid_copy[row_index])
        for col_index in range(num_columns):
            if grid_copy[row_index][col_index] == "S":
                grid_copy[row_index][col_index] = emoji["S"]
            elif grid_copy[row_index][col_index] == "*":
                grid_copy[row_index][col_index] = emoji['*']
            elif grid_copy[row_index][col_index] == "F":
                grid_copy[row_index][col_index] = emoji["F"]
            elif grid_copy[row_index][col_index] == "-":
                grid_copy[row_index][col_index] = emoji[" "]
            a_row += f'{grid_copy[row_index][col_index]}'
        print(a_row)

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    return [rows, cols]

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    if position[0] < grid_rows and position[0] >= 0:
        if position[1] < grid_cols and position[1] >= 0:
            return True
    else:
        return False
    
def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:
        directions.append('east')
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('south')
    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
        directions.append('west')
    return directions

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    valid_direction = look_around(grid, player_position)
    if direction in valid_direction:
        if direction == "north":
            player_position[0] = player_position[0] - 1
        elif direction == "east":
            player_position[1] = player_position[1] + 1
        elif direction == "south":
            player_position[0] = player_position[0] + 1
        elif direction == "west":
            player_position[1] = player_position[1] - 1
        return True
    return False

def check_finish(grid: list[list[str]], player_position: list[int, int]) -> bool:
    """
    Checks if the player has reached the exit.
    """
    if grid[player_position[0]][player_position[1]] == "F":
        return True
    return False

def display_help(file_name) -> None:
    """
    Displays a list of commands.
    """
    file = open(file_name, "r")
    text = file.read()
    print(text)

def main():
    """
    Main entry point for the game.
    """
    map_file = load_map(MAP_FILE)
    starting_position = find_start(map_file)
    while True:
        valid_direction = look_around(map_file, starting_position)
        print(f"You can go {', '.join(valid_direction)}")
        user_input = get_command()
        user_input = user_input.split()
        if user_input[0] == "escape":
            break
        elif ' '.join(user_input) == "show map":
            display_map(map_file, starting_position)
        elif user_input[0] == "go":
            if user_input[1] in valid_direction:
                move(user_input[1], starting_position, map_file)
                print(f"You moved {user_input[1]}")
            else:
                print("There is no way there.")
        elif user_input[0] == "help":
            display_help(HELP_FILE)
        else:
            print("I do not understand.")
        if check_finish(map_file, starting_position):
            print("Congratulations! You have reached the exit!")
            break 

if __name__ == '__main__':
    main()

