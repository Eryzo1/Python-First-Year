def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    counter = 0
    matrix = []
    file = open(filename, "r")
    text = file.read()
    text = text.split()
    rows = text[0]
    cols = text[1]
    text=text[2:]
    for i in range(int(rows)):
        matrix.append([])
        for j in range(int(cols)):
            matrix[i].append(int(text[counter]))
            counter += 1
    return matrix

def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values
    """
    num_rows = len(grid)
    for row_index in range(num_rows):
        a_row = ''
        num_columns = len(grid[row_index])
        for col_index in range(num_columns):
            a_row += f'{str(grid[row_index][col_index]):9}'
        print(a_row)

def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("SimCity Land Values:")
    display_grid(grid)

main()