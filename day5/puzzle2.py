# Day-5 Puzzle-2 : Cafeteria

import time

def list_of_input():
    file_path = 'day5/puzzle_input.txt'
    list_of_ranges = [] 
    with open(file_path, 'r') as file:
        content = file.read()
        sections = content.split('\n\n') # splits the input into two parts - ranges and ids - into strings
        # ranges need to be split by \n and - 
        ranges = sections[0].split('\n')
        for r in ranges:
            numbers_of_ranges = r.split('-') # stores the values in numbers_of_ranges as list of strings
            # each element in the list of strings needs to be changed to int
            # hence, make a new list where each string element is converted to int
            # if this is not done, then while sorting in the next function
            # strings will get sorted rather than number
            # meaning first element in string will be checked - 10 becomes less than 3, as 1 is the first element in string 10
            numbers_of_ranges_int = [int(numbers_of_ranges[0]), int(numbers_of_ranges[1])] 
            list_of_ranges.append(numbers_of_ranges_int) # stores each range as a list in the list_of_ranges
    print(list_of_ranges)
    return get_count_of_range_values(list_of_ranges)

def get_count_of_range_values(list_of_ranges):
    ''' Each value in all the ranges needs to counted. 
    If the value is repeated, then it should not be counted again. '''

    # sort function has the argument 'key'
    # this is defined as any anonymous function 'lambda', which takes one argument 'inner_list' 
    # inner_list[0] takes the first element of each inner_list
    list_of_ranges.sort(key = lambda inner_list : inner_list[0])
    print(list_of_ranges)
    # storing first range values
    lower_bound = list_of_ranges[0][0]
    upper_bound = list_of_ranges[0][1]
    count = 0
    for index, each_range in enumerate(list_of_ranges):
        # each_range is a pair of lower_bound and upper_bound values as a list
        next_lower_bound = each_range[0] 
        next_upper_bound = each_range[1]
        if upper_bound >= next_lower_bound:
            # merging the ranges; there will be two cases:
            # first case - when upper_bound is smaller than the next_upper_bound; eg: [3,5] [4,7]
            # this will need to create a range of [3,7]
            # second case - when when upper_bound is equal to or bigger than the next_upper_bound; eg: [3,10] [4,7]
            # this will need to create a range of [3,10]
            # hence the maximum from these two cases needs to be selected
            upper_bound = max(upper_bound, next_upper_bound)            
        elif upper_bound < next_lower_bound:
            # there might be a third case: where the upper_bound is smaller than next_lower_bound; eg: [3,10] [12,15]
            # at this time, count the previous combined range values 10-3 = 7; but 10 needs to be counted as well, hence 7+1 = 8 numbers 
            count += upper_bound - lower_bound + 1
            # when this case occurs, shift the lower_bound and upper_bound values to the new values [12,15]
            # and continue the loop
            lower_bound = next_lower_bound
            upper_bound = next_upper_bound
        if index == len(list_of_ranges) - 1:
            # exception case: when the list reaches the last range, there will be nothing further in the list 
            # for the loop to proceed - meaning the loop will end here without counting the last range values
            # hence count is done here for the last range values
            count += upper_bound - lower_bound + 1
    return count

start_time = time.time()
print(list_of_input())
end_time = time.time()
print(f"Time to run the code: {end_time - start_time} seconds.")