# Day-1 Puzzle-2 : Secret Entrance

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
  If while rotation, it passes zero, increase the count.'''

  current_number = 50
  total_count_of_zeros = 0
  zeros_in_each_rotation = 0
  for each_entry in entries: # checking if the first letter is L or R for left or right rotation
    print(each_entry)
    if each_entry[0] == 'L':
      rotation_value = int(each_entry[1:])
      if current_number == 0: # this is used because while left rotation, when the previous iteration stops at 0, the count of zeros is increased by 1.
        total_count_of_zeros -= 1
      current_number, zeros_in_each_rotation = rotation(-rotation_value, current_number)
      if current_number == 0: # this is used because while left rotation, when the iteration stops at 0, the count of zeros is not getting increased by 1.
        total_count_of_zeros += 1
    if each_entry[0] == 'R':
      rotation_value = int(each_entry[1:])
      current_number, zeros_in_each_rotation = rotation(rotation_value, current_number)
    total_count_of_zeros += zeros_in_each_rotation    
  return total_count_of_zeros

def rotation(rotation_value, current_number):
  ''' Rotation needs to be done. For left rotation, the rotational value will be negative,
  meaning as the rotation reached -1, the number becomes 99. And for right rotation, the rotational
  value will be positive, meaning as the rotation reaches 100, the number becomes 0. '''

  number_after_rotation = (current_number + rotation_value) % 100 # % will alwyas keep the number in range - 0 to 99. 
  print(f'Number after rotation is {number_after_rotation}')
  count_of_zeros = abs((current_number + rotation_value) // 100) # absolute is used to remove the negative sign. Here, whenever the value increases after 100, that means it passed zero. And whenever the value decreases below 0, that means it passed zero. 
  return number_after_rotation, count_of_zeros

print(list_of_input())