# Day-1 Puzzle-1 : Secret Entrance

""" Save the input as a txt file. Store it in your drive. Access the file from your drive. And convert it to a list"""
def list_of_input():
  file_path = 'day1/puzzle1_input.txt'
  entries = []
  with open(file_path, 'r') as file:
    for line in file:
      entries.append(line.strip()) # append is used to add each line to the list, and strip to remove the \n in every line. The strip distributes the entries whenever there is a new line
  print(entries)
  current_number = 50
  count_of_zeros = 0
  for each_entry in entries: # checking if the first letter is L or R for left or right rotation
    print(each_entry)
    if each_entry[0] == 'L':
      only_number = int(each_entry[1:])
      current_number = rotation(-only_number, current_number)
    if each_entry[0] == 'R':
      only_number = int(each_entry[1:])
      current_number = rotation(only_number, current_number)
    if current_number == 0:
      count_of_zeros += 1
  return count_of_zeros

def rotation(only_number, current_number):
  number_after_rotation = (current_number + only_number) % 100 
  print(f'Number after right rotation is {number_after_rotation}')
  return number_after_rotation

print(list_of_input())