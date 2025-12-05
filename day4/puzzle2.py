# Day-4 Puzzle-2 : Printing Department

import time

def list_of_input():
    file_path = 'day4/puzzle_input.txt'
    char_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            # each line in the input is stored as a string in the list named line_entries.
            line_entries = list(line.strip()) 
            # each char in every line is stored as an element in entries
            char_entries.append(line_entries)
    print(char_entries)
    overall_count = 0
    grid = char_entries[:]
    while True:
        # only the first iteration needs to have char_entries as input.
        # from the second iteration, the changed grid becomes the input.
        # this changed grid gets stored in grid on the left hand side in line 17.
        # for the next iteration, this left hand side 'grid' will become the input for the right hand side 'grid'.
        count_of_grid, grid = get_count_for_grid_and_new_grid(grid)
        if count_of_grid == 0:
            # the loop needs to stop when the new grid created will be same as the old grid created.
            # when this happens, the count will not increase; it will remain zero.
            break
        overall_count += count_of_grid
    return overall_count


def get_count_for_grid_and_new_grid(grid):
    ''' For each value in the line_entries when it is '@', its eight adjacent positions need to be checked.
    In these adjacent positions, there should be less than four '@' for the value to be considered.
    When this condition occurs, change the element '@' to '.'. Store this as a new 2d array, for it to be reused. 
    Eg: 1 2 3       (x-1,y-1) (x-1,y) (x-1,y+1)
        4 5 6       (x,y-1)    (x,y)    (x,y+1) 
        7 8 9       (x+1,y-1) (x+1,y) (x+1,y+1) 
        Here, for number 1, the adjacent positions are 2,5,4. 
        For number 2, the adjacent positions are 1,4,5,6,3.
        Similarly, for number 5, the adjacent positions are 1,2,3,4,6,7,8,9.
        All the edge numbers are exceptional cases.'''
    
    overall_count = 0
    new_2d_array = grid[:]
    for x, each_line in enumerate(grid): 
        # x will be line from top to bottom
        for y, each_value in enumerate(each_line):
            # y will be line from left to right
            if each_value == '@':
                count = 0
                for row_index in [x-1, x, x+1]:
                    # check the values from above to below of x,y
                    if row_index < 0 or row_index > len(grid) - 1:
                        # check for edge values
                        continue
                    for column_index in [y-1, y, y+1]:
                        # check the values from left to right of x,y
                        if column_index < 0 or column_index > len(each_line) - 1:
                            # check for edge values
                            continue
                        if x == row_index and y == column_index:
                            # removes the centre value x,y as we do not need to count this
                            continue
                        if grid[row_index][column_index] == '@':
                            count += 1
                if count < 4:
                    overall_count += 1
                    # replace the element '@' with '.' to generate a new grid
                    new_2d_array[x][y] = '.'
    return overall_count, new_2d_array

start_time = time.time()
print(list_of_input())
end_time = time.time()
print(f'Time taken to run the program is {end_time - start_time} seconds.')
