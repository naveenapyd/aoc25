# Day-2 Puzzle-1 : Gift Shop

def list_of_input():
    ''' To store the input data in a list: 
    Store the input in a txt file.
    Give the file path where you have your input data stored. Open the file in read mode.
    Using a loop, go through all entries in the file.
    Use comma to split the entries and add the entries to a list. '''

    file_path = 'day2/puzzle_input.txt'
    entries = []
    with open(file_path, 'r') as file:
        for each_entry in file:
            ranges = each_entry.split(',') # split function splits the values using comma. 
            for r in ranges:   
                numbers = r.split('-') # split function splits the values using hyphen. 
                entries.extend(numbers) # extend adds each number as a value in the list entries. Using append here will add numbers as another in the list entries.
    print(entries)
    return range_values(entries)

def range_values(entries):
    ''' Access the range of numbers present between first entry and second entry.
    Similarly, between third and fourth, and fifth and sixth and so on.
    Both first and second values should be inclusive. '''
    
    all_entries_range_values = []
    for index in range(0, len(entries), 2): # this will skip the index from 0 to 2 to 4 and so on.
        starting_value_in_range = int(entries[index]) # entries list has stored values as string. Hence convert to int.
        ending_value_in_range = int(entries[index + 1]) # index + 1 will give the odd value
        current_range_values = list(range(starting_value_in_range, ending_value_in_range + 1)) # ending_value_in_range + 1 is done because for range function, the upper limit is exclusive.
        all_entries_range_values.extend(current_range_values)
    print(all_entries_range_values)
    return all_entries_range_values

def sum_of_invalid_entries():
    ''' Check if each number stored from all the range values is legibile or not for the Gift Shop.
    To do this - check the length of the number. This is applicable to only even length numbers.
    But the numbers starting with zero should not be considered. Split the number in half. 
    Then check if the first half is equal to the second half.
    If they are equal, then find the sum of all these numbers.'''
    
    all_entries_range_values = list_of_input()
    sum = 0
    for each_value in all_entries_range_values:
        number = str(each_value) # all_entries_range_values list has stored values as int. Hence convert to string.
        if len(number) % 2 == 0 and number[0] != '0': 
            midpoint = len(number) // 2 
            first_half = number[:midpoint] 
            # if the number has 10 digits, then the first_half will be from 0 to 5 (5 being exclusive) 
            second_half = number[midpoint:]
            # the second_half will be from 5 (as 5 is exclusive in first_half) to 9
            if first_half == second_half:
                sum += int(number)
    return sum    

print(sum_of_invalid_entries())