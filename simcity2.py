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

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    rows = len(grid)
    cols = len(grid[0])
    neighbours = []

    for i in range(row-1, row+2):  # x-1, x, x+1
        for j in range(col-1, col+2):  # y-1, y+1
            if i == row and j == col:
                continue  # skip location of ‘E’
            if i < 0 or i >= rows or j < 0 or j >= cols:
                continue  # skip if location is outside the grid
            neighbours.append(grid[i][j])
    return neighbours

def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("SimCity Land Values:")
    display_grid(grid)

if __name__ == "__main__":
    main()
