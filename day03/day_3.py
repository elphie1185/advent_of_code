import math
import re

with open("day03/input.txt") as f:
    lines = [line.strip() for line in f]

def substring(row_num: int, col_start: int, col_end: int) -> str:  # y1 is inclusive, y2 is exclusive
    return lines[row_num][max(col_start, 0):min(col_end, len(lines[0]))] if row_num >= 0 and row_num < len(lines) else ""

def find_adjacent_charaters(number, row_num):
    left_neighbor_coor = number.start() - 1
    right_neighbor_coor = number.end()
    adjacent_characters = \
        substring(row_num-1, left_neighbor_coor, right_neighbor_coor + 1) + \
        substring(row_num, left_neighbor_coor, left_neighbor_coor + 1) + \
        substring(row_num, right_neighbor_coor, right_neighbor_coor + 1) + \
        substring(row_num+1, left_neighbor_coor, right_neighbor_coor + 1)
    return adjacent_characters

def is_part_number(number, row_num): 
    return set(find_adjacent_charaters(number, row_num)) != {'.'}

###########################################################
#
#  PART 1
#
###########################################################

part_numbers = [
    int(number.group())
    for row_num, line in enumerate(lines)
    for number in re.finditer(r"\d+", line)
    if is_part_number(number, row_num)
]

# print(sum(part_numbers))

###########################################################
#
#  PART 2
#
###########################################################

parts_coordinates = {}
for row_num, line in enumerate(lines):
    for number in re.finditer(r"\d+", line):
        if is_part_number(number, row_num):
            part_number = int(number.group())
            for col_num in range(number.start(), number.end()):
                parts_coordinates[(row_num, col_num)] = part_number

gear_ratios = []
for gear_row, line in enumerate(lines):
    for gear in re.finditer("\*", line):
        gear_col = gear.start()
        adjacent_coordinates = [
            (row, col) for row in range(gear_row-1, gear_row+2) for col in range(gear_col-1, gear_col+2)
            if (row, col) != (gear_row, gear_col)
            and row >= 0 and row < len(lines)
            and col >= 0 and col < len(line)
        ]
        adjacent_parts = set(
            [parts_coordinates[x_y]
            for x_y in adjacent_coordinates if x_y in parts_coordinates]
        )

        if len(adjacent_parts) == 2:
            gear_ratios.append(math.prod(adjacent_parts))

print(sum(gear_ratios))