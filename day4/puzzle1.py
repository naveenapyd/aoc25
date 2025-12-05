# Day-4 Puzzle-1 : Printing Department

def list_of_input():
    file_path = 'day4/puzzle_input.txt'
    line_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            # each line in the input is stored as a string in line_entries.
            line_entries.append(line.strip()) # append is used to add each line to the list, and strip to remove the \n in every line. The strip distributes the entries whenever there is a new line
    print(line_entries)
    return adjacent_positions(line_entries)

def adjacent_positions(line_entries):
    ''' For each value in the line_entries when it is '@', its eight adjacent positions need to be checked.
    In these adjacent positions, there should be less than four '@' for the value to be considered. 
    Eg: 1 2 3       (x-1,y-1) (x-1,y) (x-1,y+1)
        4 5 6       (x,y-1)    (x,y)    (x,y+1) 
        7 8 9       (x+1,y-1) (x+1,y) (x+1,y+1) 
        Here, for number 1, the adjacent positions are 2,5,4. 
        For number 2, the adjacent positions are 1,4,5,6,3.
        Similarly, for number 5, the adjacent positions are 1,2,3,4,6,7,8,9.
        All the edge numbers are exceptional cases.'''
    
    overall_count = 0
    for x, each_line in enumerate(line_entries): 
        # x will be line from top to bottom
        for y, each_value in enumerate(each_line):
            # y will be line from left to right
            if each_value == '@':
                count = 0
                for row_index in [x-1, x, x+1]:
                    # check the values from above to below of x,y
                    if row_index < 0 or row_index > len(line_entries) - 1:
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
                        if line_entries[row_index][column_index] == '@':
                            count += 1
                if count < 4:
                    overall_count += 1
    return overall_count

print(list_of_input())
