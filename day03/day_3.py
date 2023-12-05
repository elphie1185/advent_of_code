import re

not_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

with open("day03/input.txt") as f:
    lines = [line for line in f]

print(lines[0])

# get indices of the numbers for each row
line_numers_indices = [
    [
        {
            "i_start": m.start(),
            "i_end": m.end(),
            "number": int(m.group())
        }
        for m in re.finditer("\d+", line)
    ]
    for line in lines
]
print(len(lines), len(line_numers_indices))


#  check indice before and below for characters different from dot or num

# get array of characters in rows above and below at indices -1 and +1
#  check if any of the characters are different from a dot or a number
# row_above = []
# row_below = []

# all(character in not_symbols for character in row_below)
