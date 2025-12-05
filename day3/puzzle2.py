# Day-3 Puzzle-2 : Lobby

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
  ''' Each entry is checked for the largest possible twelve digit number present in it. 
   This is done by checking the first element, and checking the maximum of the elements after it.
   Then second element with the maximum of the elements after it and so on. '''
  
  sum = 0
  for each_entry in entries:
    twelve_digit_number = ['0'] * 12 # twelve digit number representation.
    index_of_max_digit = -1 # first iteration for loop at line 33 should start with 0.
    for index_of_twelve_digit_number in range(12): # each position for the twelve digit number.
      # for the loop below: first digit will be between 0 and len - 12 + 1; this checks till the last 12th digit, as after that there will be no 12 digits to check.
      # second digit will be between position of the first digit found and len - 11 + 1; this checks till the last 11th digit, as after that there will be no more 11 digits to check.
      # and so on. For a better understanding of these iterations, check out the docstring from line 41.
      for index in range(index_of_max_digit + 1, len(each_entry) - (12 - index_of_twelve_digit_number) + 1):
        if int(each_entry[index]) > int(twelve_digit_number[index_of_twelve_digit_number]): # checking the highest digit from the number
            twelve_digit_number[index_of_twelve_digit_number] = each_entry[index]
            index_of_max_digit = index # storing index for further iterations, as this will decide the start of the range for this loop.
    final_number = ''.join(twelve_digit_number) # joining the string of numbers, because the twelve_digit_number will be a list of digits as strings. Eg: ['1','3','9']. This should be '139'
    sum += int(final_number)
  return sum

'''for index in range(len(each_entry)-12 + 1): # checks the digits till the last 12th digit, as after that there will be no 12 digits to check.
    if int(each_entry[index]) > int(twelve_digit_number[0]):
    twelve_digit_number[0] = each_entry[index]
    index_of_max_digit = index
for index in range(index_of_max_digit + 1, len(each_entry)-11 + 1):
    if int(each_entry[index]) > int(twelve_digit_number[1]):
    twelve_digit_number[1] = each_entry[index]
    index_of_max_digit = index
for index in range(index_of_max_digit + 1, len(each_entry)-10 + 1):
    if int(each_entry[index]) > int(twelve_digit_number[2]):
    twelve_digit_number[2] = each_entry[index]
    index_of_max_digit = index
for index in range(index_of_max_digit + 1, len(each_entry)-9 + 1):
    if int(each_entry[index]) > int(twelve_digit_number[3]):
    twelve_digit_number[3] = each_entry[index]
    index_of_max_digit = index
and so on...'''

start_time = time.time()
print(list_of_input())
end_time = time.time()
print(f'Time taken to run the program is {end_time - start_time} seconds.')