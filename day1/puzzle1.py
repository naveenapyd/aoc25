# Day-1 Puzzle-1 : Secret Entrance

def list_of_input():
  ''' To store the input data in a list: 
    Store the input in a txt file.
    Give the file path where you have your input data stored. Open the file in read mode.
    Using a loop, go through all entries in the file.
    Use comma to split the entries and add the entries to a list. '''

  file_path = 'day1/puzzle_input.txt'
  entries = []
  with open(file_path, 'r') as file:
    for line in file:
      entries.append(line.strip()) # append is used to add each line to the list, and strip to remove the \n in every line. The strip distributes the entries whenever there is a new line
  print(entries)
  return number_of_zeros(entries)

def number_of_zeros(entries):
  ''' The iteration starts at 50. Depending on left or right, the rotation occurs.
  Each time the rotation happens, the number where it stops changes. 
  When the rotation stops at the number zero, increase the count.'''

  current_number = 50
  count_of_zeros = 0
  for each_entry in entries: # checking if the first letter is L or R for left or right rotation
    print(each_entry)
    if each_entry[0] == 'L':
      rotational_value = int(each_entry[1:])
      current_number = rotation(-rotational_value, current_number) # sending negative value for left rotation
    if each_entry[0] == 'R':
      rotational_value = int(each_entry[1:])
      current_number = rotation(rotational_value, current_number)
    if current_number == 0:
      count_of_zeros += 1
  return count_of_zeros

def rotation(rotational_value, current_number):
  ''' Rotation needs to be done. For left rotation, the rotational value will be negative,
  meaning as the rotation reached -1, the number becomes 99. And for right rotation, the rotational
  value will be positive, meaning as the rotation reaches 100, the number becomes 0. '''

  number_after_rotation = (current_number + rotational_value) % 100 # % will alwyas keep the number in range - 0 to 99.
  print(f'Number after right rotation is {number_after_rotation}')
  return number_after_rotation

print(list_of_input())