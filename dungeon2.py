import copy
MAP_FILE = 'cave_map.txt'

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
    grid_copy = copy.deepcopy(grid)
    grid_copy[player_position[0]][player_position[1]] = "@"
    num_rows = len(grid_copy)
    for row_index in range(num_rows):
        a_row = ''
        num_columns = len(grid_copy[row_index])
        for col_index in range(num_columns):
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

def main():
    """
    Main entry point for the game.
    """
    map_file = load_map(MAP_FILE)
    starting_position = find_start(map_file)
    valid_direction = look_around(map_file, starting_position)
    while True:
        print(f"You can go {', '.join(valid_direction)}")
        user_input = get_command()
        if user_input == "escape":
            break
        elif user_input == "show map":
            display_map(map_file, starting_position)
        else:
            print("I do not understand.")

if __name__ == '__main__':
    main()

