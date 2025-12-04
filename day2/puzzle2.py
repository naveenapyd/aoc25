# Day-2 Puzzle-2 : Gift Shop

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
            ranges = each_entry.split(',') # split function splits the values using comma. append function adds the values as an entry to the list.
            for r in ranges:   
                numbers = r.split('-') # split function splits the values using hyphen. append function adds the values as an entry to the list.
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
    To do this - check the length of the number. Then split the number digit wise and create a new number 
    with that digit repeated. If this new number is equal to the original number, then add up as we need the sum.
    Eg: If the number is 121212, then the code first checks the first digit '1', and it will create a new number
    as 111111. As this is not equal to the original number, it will then check the first two digits '12' and create
    a new number 121212. As this is equal to the original number, it will get added up.
    This digit wise split can be done till the middle of the number, as there can't be any repeting units 
    after the middle.
    Eg: If the number is 123124, then there is no point in checking 1231. It is sufficient to check till 123.'''
    
    all_entries_range_values = list_of_input()
    sum = 0
    for value in all_entries_range_values:
        number = str(value) # all_entries_range_values list has stored values as int. Hence convert to string.
        midpoint = len(number) // 2
        # range till midpoint of the number is considered because after it the number cannot have a repeating pattern.
        # so if there are six digits in the number, the range will check if the first digit is repeating, them first two digits, then first three digits, and stop.
        for repeated_digit in range(1, midpoint + 1): 
            if len(number) % repeated_digit == 0: # this will check the first digit, then second, and so on, till midpoint.
                number_of_repetitions = len(number) // repeated_digit
                if number[:repeated_digit] * number_of_repetitions == number: # this will concatenate the repeated digit by number of repetition times, and check if this new number created is equal to the original number.
                    print(int(number))
                    sum += int(number)
                    break # this is required to break from the inner loop. Eg: if the number is 2222, the inner loop is true for two cases '2' and '22', because of which 2222 will get added twice.
    return sum

print(sum_of_invalid_entries())
