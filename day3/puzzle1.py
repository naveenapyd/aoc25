# Day-3 Puzzle-1 : Lobby

import time

def list_of_input():
  ''' To store the input data in a list: 
    Store the input in a txt file.
    Give the file path where you have your input data stored. Open the file in read mode.
    Using a loop, go through all entries in the file.
    Use comma to split the entries and add the entries to a list. '''

  file_path = 'day3/puzzle_input.txt'
  entries = []
  with open(file_path, 'r') as file:
    for line in file:
      entries.append(line.strip()) # append is used to add each line to the list, and strip to remove the \n in every line. The strip distributes the entries whenever there is a new line
  print(entries)
  return largest_possible_joltage(entries)

def largest_possible_joltage(entries):
  ''' Each entry is checked for the largest possible double digit number present in it. 
   This is done by checking the first element with all the elements after it.
   Then second element with the elements after it and so on. '''
  
  sum = 0
  for each_entry in entries:
    all_numbers_in_each_entry = []
    for index in range(len(each_entry)): 
      for other_index in range(index + 1, len(each_entry)): # checks all other elements after the element first selected. 
        two_digit_number_str = each_entry[index] + each_entry[other_index]
        two_digit_number_int = int(two_digit_number_str)
        all_numbers_in_each_entry.append(two_digit_number_int)
    largest_possible_number = max(all_numbers_in_each_entry)
    # print(largest_possible_number)
    sum += largest_possible_number
    # print(sum)
  return sum


start = time.time()
print(list_of_input())
stop = time.time()
print(stop - start)
