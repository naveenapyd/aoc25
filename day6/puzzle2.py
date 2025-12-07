# Day-6 Puzzle-2 : Trash Compactor

import time

def list_of_input():
    file_path = 'day6/puzzle_input.txt'    
    line_entries = []
    symbol = []
    with open(file_path, 'r') as file:
        for line in file:
            values_in_line = line.strip('\n') # removing only the \n character, as we need spaces here
            line_entries.append(values_in_line) 
        symbol = line_entries[-1].split() # creating a new list for the last row symbols, and .split() will remove anyy leading or trailing whitespaces 
        line_entries = line_entries[:-1] # only the values are stored as a separate list; each row in the list is a string of numbers including whitespace
    print(line_entries)
    print(symbol)
    return get_total_count_of_worksheet(line_entries, symbol)

def get_total_count_of_worksheet(line_entries, symbol):
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
    sum = 0
    product = 1
    symbol_index = len(symbol) - 1 # storing this value as the symbol needs to be changed
    for y in range(len(line_entries[0]) - 1, 0 - 1, -1):
        # this will give the range of values from left to right - y values
        # len(line_entries[0] - 1) will give the last value
        # range is done in reverse order - from last to first, and consider each element in reverse order
        number = '' # to store the number generated from top to bottom
        for x in range(len((line_entries))):
            # this will give the range of values from top to bottom - x values
            # if there is an empty space in a column containing a number, then skip that and proceed to the next space
            if line_entries[x][y] == ' ':
                continue
            number += line_entries[x][y] # concatenate the string numbers (from top to bottom)
        if len(number) == 0: 
            # when the entire column is space, i.e., it is an empty string from top to bottom
            # it means that the next symbol starts for the next set of numbers
            # hence total_count needs to be increased at this point
            if symbol[symbol_index] == '+':
                total_count += sum
            elif symbol[symbol_index] == '*':
                total_count += product 
            symbol_index -= 1 # symbol_index to be changed to the next one in reverse order
            sum = 0
            # reset these values for the next iteration of y
            product = 1
            continue # loop should start for the next iteration of y  
        # when the column is not space, or until the space occurs, the numbers generated
        # from top to bottom need to either added or multiplied
        if symbol[symbol_index] == '+':
            sum += int(number)
        elif symbol[symbol_index] == '*':
            product *= int(number)
        if y == 0:
            # in the previous section, the total_count increases only after an empty column is found
            # for the last column in the loop, i.e., the first column in the list, the list ends
            # and there will be no empty column after that, which means this will not be added to total_count
            # hence, total_count in increased for the first column of the list here
            if symbol[symbol_index] == '+':
                total_count += sum
            if symbol[symbol_index] == '*':
                total_count += product 
    return total_count       

start_time = time.time()
print(list_of_input())
end_time = time.time()
print(f'Time to run the code: {end_time - start_time} seconds.')
