# Day-5 Puzzle-1 : Cafeteria

def list_of_input():
    file_path = 'day5/puzzle_input.txt'
    list_of_ranges = [] 
    list_of_ids = []
    with open(file_path, 'r') as file:
        content = file.read()
        sections = content.split('\n\n') # splits the input into two parts - ranges and ids - into strings
        # ranges need to be split by \n and - 
        ranges = sections[0].split('\n')
        for r in ranges:
            numbers_of_ranges = r.split('-')
            list_of_ranges.extend(numbers_of_ranges)
        # ids need to be split by \n
        list_of_ids = sections[1].split('\n')
    print(list_of_ranges)
    print(list_of_ids)
    return get_count_of_overlapping_values(range_values(list_of_ranges), list_of_ids)

def range_values(list_of_ranges):    
    ''' Access the range of numbers present between first entry and second entry.
    Similarly, between third and fourth, and fifth and sixth and so on.
    Both first and second values should be inclusive. '''

    ''' Storing all the range values in a list for the unique input is throwing a Memory Error.
    However the code worked for the given test input. '''

    all_range_values = []
    for index in range(0, len(list_of_ranges), 2): # this will skip the index from 0 to 2 to 4 and so on.
        starting_value_in_range = int(list_of_ranges[index]) # entries list has stored values as string. Hence convert to int.
        ending_value_in_range = int(list_of_ranges[index + 1]) # index + 1 will give the odd value
        current_range_values = list(range(starting_value_in_range, ending_value_in_range + 1)) # ending_value_in_range + 1 is done because for range function, the upper limit is exclusive.
        all_range_values.extend(current_range_values)
    print(all_range_values)
    return all_range_values
    
def get_count_of_overlapping_values(all_range_values, list_of_ids):
    ''' Each character in list_of_ids is checked if it is present in all_range_values.
    If present then it is counted. '''

    count = 0
    for id in list_of_ids:
        if int(id) in all_range_values:
            count += 1
    return count

print(list_of_input())