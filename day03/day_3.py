import re

with open("day03/input.txt") as f:
    lines = [line.strip() for line in f]


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

def find_pattern_per_row(pattern, lines):
    return [
        [
            {
                "row_index": row,
                "i_start": int(m.start()),
                "i_end": int(m.end()),
                "number": m.group()
            }
            for m in re.finditer(pattern, line)
        ]
        for row, line in enumerate(lines)
    ]


###########################################################
#
#  PART 1
#
###########################################################

# useful variables
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
not_symbols = numbers + ["."]
last_row_num = len(lines)-1
last_column_num = len(lines[0])-1

# get indices of the numbers for each row
numbers_indices_per_row = find_pattern_per_row("\d+", lines)

#  check if there are symbols surrounding numbers
valid_numbers = []
for row_number, line_numbers in enumerate(numbers_indices_per_row):
    rows_to_check = get_rows_to_check(row_number)
    for item in line_numbers:
        rows_index_to_check = [
            get_row_at_indices_range(row, item["i_start"], item["i_end"])
            for row in rows_to_check
        ]
        if not all(char in not_symbols for index_row_to_check in rows_index_to_check for char in index_row_to_check):
            valid_numbers.append(int(item["number"]))
print(sum(valid_numbers))

###########################################################
#
#  PART 2
#
###########################################################

# get indices of the stars for each row
star_indices_per_row = find_pattern_per_row("\*", lines)
# print(star_indices_per_row[:10])

# check if the stars are surrounded by numbers and if they are surrounded by 2 numbers get them
#  check if there are symbols surrounding numbers
valid_numbers = []

for row_number, line_numbers in enumerate(star_indices_per_row):
    rows_to_check = get_rows_to_check(row_number)
#     rows_index_to_check = [
#         get_row_at_indices_range(row, line_numbers["i_start"], line_numbers["i_end"])
#         for row in rows_to_check
#     ]
#     print(rows_index_to_check)
#     has_numbers = [any(char in numbers for char in row) for row in rows_index_to_check]
#     print(sum(has_numbers))
    # num_array = any(char in numbers for char in rows_index_to_check)
    # print(num_array)


# for row_number, line_numbers in enumerate(star_indices_per_row):
#     rows_to_check = get_rows_to_check(row_number)
#     for item in line_numbers:
#         rows_index_to_check = [
#             get_row_at_indices_range(row, item["i_start"], item["i_end"])
#             for row in rows_to_check
#         ]
        # if sum(any(char in numbers for index_row_to_check in rows_index_to_check for char in index_row_to_check):
        #     valid_numbers.append(int(item["number"]))
# print(sum(valid_numbers))

