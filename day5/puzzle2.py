# Day-5 Puzzle-2 : Cafeteria

def list_of_input():
    file_path = 'day5/puzzle_input.txt'
    list_of_ranges = [] 
    with open(file_path, 'r') as file:
        content = file.read()
        sections = content.split('\n\n') # splits the input into two parts - ranges and ids - into strings
        # ranges need to be split by \n and - 
        ranges = sections[0].split('\n')
        for r in ranges:
            numbers_of_ranges = r.split('-')
            list_of_ranges.extend(numbers_of_ranges)
    print(list_of_ranges)
    return get_count_of_range_values(list_of_ranges)

def get_count_of_range_values(list_of_ranges):
    ''' Each value in all the ranges needs to counted. 
    If the value is repeated, then it should not be counted again. '''

    all_values_set = set()
    for index in range(0, len(list_of_ranges), 2):
        lower_bound = int(list_of_ranges[index])
        upper_bound = int(list_of_ranges[index + 1])
        # all range values are updated in a set; a set does not store duplicate values
        all_values_set.update(range(lower_bound, upper_bound + 1))            
    return len(all_values_set)

print(list_of_input())

