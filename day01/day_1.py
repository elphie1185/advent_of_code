import regex as re

digit_string_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

digit_patterns = "|".join(list(digit_string_dict.keys())+["\d"])

with open("day01/day_1_input.txt") as f:
    lines = [line for line in f]

all_digits = [re.findall(
    digit_patterns,
    text,
    overlapped=True
    ) for text in lines
]

all_digits_replaced = [
    list(map(digit_string_dict.get, digit, digit))
    for digit in all_digits
]
number_strings = [digit[0]+digit[-1] for digit in all_digits_replaced]
numbers = [int(number_string) for number_string in number_strings]

print(sum(numbers))
