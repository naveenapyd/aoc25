# Day-1 Puzzle-2 : Secret Entrance

""" Save the input as a txt file. Store it in your drive. Access the file from your drive. And convert it to a list"""
def list_of_input():
  file_path = 'day1/puzzle1_input.txt'
  entries = []
  with open(file_path, 'r') as file:
    for line in file:
      entries.append(line.strip()) # append is used to add each line to the list, and strip to remove the \n in every line. The strip distributes the entries whenever there is a new line
  print(entries)
  current_number = 50
  total_count_of_zeros = 0
  zeros_in_each_rotation = 0
  for each_entry in entries: # checking if the first letter is L or R for left or right rotation
    print(each_entry)
    if each_entry[0] == 'L':
      rotation_value = int(each_entry[1:])
      if current_number == 0:
        total_count_of_zeros -= 1
      current_number, zeros_in_each_rotation = rotation(-rotation_value, current_number)
      if current_number == 0:
        total_count_of_zeros += 1
    if each_entry[0] == 'R':
      rotation_value = int(each_entry[1:])
      current_number, zeros_in_each_rotation = rotation(rotation_value, current_number)
    total_count_of_zeros += zeros_in_each_rotation    
  return total_count_of_zeros

def rotation(rotation_value, current_number):
  number_after_rotation = (current_number + rotation_value) % 100 # % will alwyas keep the number in range - 0 to 99. 
  print(f'Number after rotation is {number_after_rotation}')
  count_of_zeros = abs((current_number + rotation_value) // 100)
  return number_after_rotation, count_of_zeros

print(list_of_input())