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
   This is done by checking the first element, and checking the maximum of the elements after it.
   Then second element with the maximum of the elements after it and so on. '''
  
  sum = 0
  for each_entry in entries:
    overall_max_for_entry = 0 
    for index in range(len(each_entry)-1): # checks till last second digit, as last digit need not be considered.
      max_second_digit = 0
      if int(each_entry[index]) < (overall_max_for_entry // 10): 
          # checks if the first digit of the maximum number found is greater than all the other remaining elements. If it is not greater, then that element need not be considered, as the double digit number it generates will not be greater.
          continue  
      for other_index in range(index + 1, len(each_entry)): # checks all other elements after the element first selected. 
        if int(each_entry[other_index]) > max_second_digit: # checks the maximum of the remaining elements for each iteration.
          max_second_digit = int(each_entry[other_index])
      two_digit_number = int(each_entry[index] + str(max_second_digit))    
      if two_digit_number > overall_max_for_entry: # checks the maximum of all the elements in each entry
        overall_max_for_entry = two_digit_number
    sum += overall_max_for_entry
  return sum

start = time.time()
print(list_of_input())
stop = time.time()
print(stop - start)