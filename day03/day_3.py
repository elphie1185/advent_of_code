import re

with open("day03/input.txt") as f:
    lines = [line.strip() for line in f]

not_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
last_row_num = len(lines)-1
last_column_num = len(lines[0])-1


def get_row_above(index): 
    row_above_index = index - 1
    return lines[row_above_index]

def get_row_below(index):
    row_below_index = index + 1
    return lines[row_below_index]

def get_rows_to_check(row_number): 
    if row_number==0: 
        return [lines[row_number], get_row_below(row_number)]
    elif row_number==last_row_num: 
        return [lines[row_number], get_row_above(row_number)]
    else: 
        row_below = get_row_below(row_number)
        row_above = get_row_above(row_number)
        return [lines[row_number], row_below, row_above]
    
def get_row_at_indices_range(row, num_start, num_end): 
    if num_start==0: 
        ix_end = num_end + 1 
        return row[num_start:ix_end]
    elif num_end==last_column_num: 
        ix_start = num_start - 1 
        return row[ix_start:num_end] 
    else: 
        ix_start = num_start - 1 
        ix_end = num_end + 1 
        return row[ix_start:ix_end]


# get indices of the numbers for each row
numbers_indices_per_row = [
    [
        {
            "i_start": int(m.start()),
            "i_end": int(m.end()),
            "number": int(m.group())
        }
        for m in re.finditer("\d+", line) 
    ]
    for line in lines
]

valid_numbers = []
for row_number, line_numbers in enumerate(numbers_indices_per_row): 
    rows_to_check = get_rows_to_check(row_number)
    # print("############")
    # print(row_number)
    # print(len(line_numbers))
    for item in line_numbers: 
        rows_index_to_check = [
            [get_row_at_indices_range(row, item["i_start"], item["i_end"])] 
            for row in rows_to_check
        ]
        if all(character in not_symbols for row_index_to_check in rows_index_to_check for character in row_index_to_check): 
            valid_numbers.append(item["number"])
print(valid_numbers)

    # print("############")
    # print(row_number)
    # print(rows_to_check)

    
# print(len(lines), len(numbers_indices_per_row), line_numers_indices[0])
# row_above_5 = get_row_above(index=5)
# print(numbers_indices_per_row[5])
# for thing in numbers_indices_per_row[5]:
#     if thing["i_start"]
#     print(row_above_5[thing["i_start"]:thing["i_end"]])

#  check indice before and below for characters different from dot or num

# print(row_above_1[3:6])

    #   ["number_indices"])
# get array of characters in rows above and below at indices -1 and +1
#  check if any of the characters are different from a dot or a number
# row_above = []
# row_below = []

# all(character in not_symbols for character in row_below)
