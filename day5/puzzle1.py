# Day-5 Puzzle-1 : Cafeteria

import time

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
    return get_count_of_overlapping_values(list_of_ranges, list_of_ids)

def get_count_of_overlapping_values(list_of_ranges, list_of_ids):
    ''' Each character in list_of_ids is checked if it is present in list_of_ranges.
    If present then it is counted. '''

    count = 0
    for id in list_of_ids:
        for index in range(0, len(list_of_ranges), 2):
            # checking a pair of values in every loop - 0th element, 2nd element, 4th element, and so on, will be all the index values
            lower_bound = int(list_of_ranges[index])
            # 0th element, 2nd element, 4th element, and so on
            upper_bound = int(list_of_ranges[index + 1])
            # 1st element, 3rd element, 5th element and so on
            if int(id) >= lower_bound and int(id) <= upper_bound:
                # cheking if the number is within the range. Eg: if range is 3-5, then number should be greater than 3 and less than 5
                count += 1
                # when the number is found, this loop should end, so that it doesn't iterate for another range which might also contain the number
                # Eg: number = 17, ranges = (16-20) and (12-18). The loop will iterate for both the ranges, and count will increase twice 
                # In order to avoid this, break statement is used
                break
    return count

start_time = time.time()
print(list_of_input())
end_time = time.time()
print(f'Time to run the code: {end_time - start_time} seconds.')
