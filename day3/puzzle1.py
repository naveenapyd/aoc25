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
  ''' Each entry is checked for the maximum double digit number in it.
  First the highest digit is checked in all the elements except the last digit, as a double digit number is needed.
  And then the highest digit in the elements after the first highest digit is checked.
  Then sum of the all these maximum double digit numbers is done.'''

  sum = 0  
  for each_entry in entries:
    max_first_digit = 0
    max_second_digit = 0
    index_of_max_digit = 0
    for index in range(len(each_entry) - 1):
        if int(each_entry[index]) > max_first_digit:
          max_first_digit = int(each_entry[index])
          index_of_max_digit = index
    for index in range(index_of_max_digit + 1, len(each_entry)):
        if int(each_entry[index]) > max_second_digit:
           max_second_digit = int(each_entry[index])
    max_two_digit_number = str(max_first_digit) + str(max_second_digit)
    sum += int(max_two_digit_number)
  return sum
  
start_time = time.time()
print(list_of_input())
end_time = time.time()
print(f'Time taken to run the program is {end_time - start_time} seconds.')