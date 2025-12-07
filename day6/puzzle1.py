# Day-6 Puzzle-1 : Trash Compactor

import time

def list_of_input():
    file_path = 'day6/puzzle_input.txt'    
    line_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            line_entries.append(line.split()) # .split() removes all the leading and trailing spaces for each element
    print(line_entries)
    return get_total_count_of_worksheet(line_entries)

def get_total_count_of_worksheet(line_entries):
    ''' Each element should be accessed column wise.
    Eg: 1 2 3       (x-1,y-1) (x-1,y) (x-1,y+1)
        4 5 6       (x,y-1)    (x,y)    (x,y+1) 
        7 8 9       (x+1,y-1) (x+1,y) (x+1,y+1) 
    1,4,7 are one subset; 2,5,8 are another; and 3,6,9 are another.
    If we want 1,2,3 then we will select values for all ranges in line_entries,
    and then go to values in each line. Now, the reverse must be done.
    Since we want 1,4,7 we will first select values for all ranges in each line,
    and then go to values in line_entries.'''

    total_count = 0
    for y in range(len(line_entries[0])): 
        # this will give the range of values from left to right - y values
        sum = 0
        product = 1
        for x in range(len(line_entries) - 1): 
            # this will give the range of values from top to bottom - x values
            # len(line_entries) - 1 is done because last entry is a symbol and does not contribute to answer
            if line_entries[-1][y] == '+':
                sum += int(line_entries[x][y])
            elif line_entries[-1][y] == '*':
                product *= int(line_entries[x][y])
        if line_entries[-1][y] == '+': 
            total_count += sum
        elif line_entries[-1][y] == '*':
            # this needs to be checked because intial product value is '1'
            # without this if statement, the total count will increase by '1' even when there is no '*'
            total_count += product
    return total_count    

start_time = time.time()
print(list_of_input())
end_time = time.time()
print(f'Time taken to run the code: {end_time - start_time} seconds.')
