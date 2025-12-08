# Day-7 Puzzle-1 : Laboratories

import time

def list_of_input():
    file_path = 'day7/puzzle_input.txt'
    line_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            # line.strip() gives a string; for a string a single element can't be replaced
            # a new string has to be created to replace a new element
            # here split() doesn't work, because there are no spaces between the characters
            # hence convert the line.strip() into a list
            # which will store each char as an element in the list
            line_entries.append(list(line.strip()))
    print(line_entries)
    return get_count_of_split(line_entries)

def get_count_of_split(line_entries):
  new_grid = line_entries[:]
  split_count = 0
  for x in range(len(new_grid)): # each row in the grid gets accessed
    for y in range(len(new_grid[0])): # each element in the grid gets accessed
      if new_grid[x][y] == 'S': # starts at S
        new_grid[x+1][y] = '|' # element right below S becomes |
      if new_grid[x][y] == '.':
        # if there is | above ., that needs to be changed to | for the split to continue
        if new_grid[x-1][y] == '|':
          new_grid[x][y] = '|'
      if new_grid[x][y] == '^':
        # split occurs when | is seen above ^
        if new_grid[x-1][y] == '|':
          new_grid[x][y-1] = '|'
          new_grid[x][y+1] = '|'
          split_count += 1
  return split_count  

start_time = time.time()
print(list_of_input())
end_time = time.time()
print(f'Time to run the code: {end_time - start_time} seconds.')