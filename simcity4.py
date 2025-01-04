'''
This program takes a 2D list and finds the average and max values.
Author: Sami Pokharel
Date: November 10, 2023
'''
# Import copy module library
import copy

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
            a_row += f'{str(grid[row_index][col_index]):>9}'  # Left alignment
        print(a_row)

def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell.
    This function I refrenced from the slides. 
    """
    rows = len(grid)
    cols = len(grid[0])
    neighbours = []

    for i in range(row-1, row+2):  # row-1, row, row+1
        for j in range(col-1, col+2):  # row-1, row+1
            if i == row and j == col:
                continue  # skip location of the value in the specific row and column
            if i < 0 or i >= rows or j < 0 or j >= cols:
                continue  # skip if location is outside the grid
            neighbours.append(grid[i][j])
    return neighbours

def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid
    Creates a new grid that is a copy of the original grid
    Call find_neighbor_values function to find the neighbors of each cell.
    Find the average of their values and round it to the nearest integer 
    Use the average values to fill in the missing values in the new grid.
    Return the new grid   
    Do NOT modify the original grid!
    """
    grid_copy = copy.deepcopy(grid)
    rows = len(grid_copy)
    cols = len(grid_copy[0])
    for i in range(rows):
        for j in range(cols):
            if grid_copy[i][j] == 0:
                neighbor_values = find_neighbor_values(grid_copy, i, j)
                average_values = round((sum(neighbor_values)/len(neighbor_values)))
                grid_copy[i][j] = average_values
    return grid_copy

def find_max(grid: list[list[int]]) -> int:
    """
    Find the max value in the grid (rounded to the nearest integer)
    """
    for i in range(len(grid)):
        max_value = round(max(grid[i]))
    return max_value

def find_average(grid: list[list[int]]) -> int:
    """
    Find the average value in the grid (rounded to the nearest integer)
    """
    sum_values = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            sum_values += grid[i][j]
    average_of_values = round(sum_values/(rows * cols))
    return average_of_values

def main():
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")

if __name__ == "__main__":
    main()