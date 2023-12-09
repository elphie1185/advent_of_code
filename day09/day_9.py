def change_str_array_to_int(array): 
    return [int(x[1:])*-1 if x.startswith("-") else int(x) for x in array]

def is_array_all_zero(array): 
    return (all(value==0 for value in array))

def get_difference_array(array): 
    return [
        (array[i+1] - array[i]) 
        for i in range(len(array) -1) 
    ]

def get_array_sequence(array): 
    array_sequence = [array]
    while not is_array_all_zero(array): 
        array = get_difference_array(array)
        array_sequence.append(array)
    return array_sequence

def append_next_sequence_value(array_sequence, direction): 
    if direction == "start": 
        for i in range((len(array_sequence)-1), 0, -1):
            next_sequence_value = -(array_sequence[i][0]) + array_sequence[i-1][0]
            array_sequence[i-1].insert(0, next_sequence_value)
    else: 
        for i in range((len(array_sequence)-1), 0, -1):
            next_sequence_value = array_sequence[i][-1] + array_sequence[i-1][-1]
            array_sequence[i-1].append(next_sequence_value)
    return array_sequence

def get_entry(updated_array_sequence, entry_index): 
    return updated_array_sequence[0][entry_index]

# read the input and convert to int
with open("day09/input.txt") as f:
    lines = [line.split() for line in f]
int_arrays = [change_str_array_to_int(line) for line in lines]


###############################################################################
#
#  PART 1
#
###############################################################################

array_sequences = [get_array_sequence(array) for array in int_arrays]
updated_array_sequences = [append_next_sequence_value(array_sequence, direction="end") for array_sequence in array_sequences]
first_row_last_entries = [get_entry(updated_array_sequence, -1) for updated_array_sequence in updated_array_sequences]

print(sum(first_row_last_entries))

###############################################################################
#
#  PART 2
#
###############################################################################

array_sequences = [get_array_sequence(array) for array in int_arrays]
new_updated_array_sequences = [append_next_sequence_value(array_sequence, direction="start") for array_sequence in array_sequences]
first_row_first_entries = [get_entry(updated_array_sequence, 0) for updated_array_sequence in new_updated_array_sequences]

print(sum(first_row_first_entries))

