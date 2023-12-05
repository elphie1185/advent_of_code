import re
import numpy as np

with open("day02/day_2_input.txt") as f:
    lines = [line for line in f]

max_red = 12
max_green = 13
max_blue = 14

colour_draws = [
    {
        "game": int(re.search("Game (.*):", line).group(1)),
        "blue_draws": [int(digit) for digit in re.findall(r"(\d+) blue", line)],
        "green_draws" : [int(digit) for digit in re.findall(r"(\d+) green", line)],
        "red_draws" : [int(digit) for digit in re.findall(r"(\d+) red", line)],
    }
    for line in lines
]

# Get the indices of the correct game
correct_games = [
    colour_draw["game"]
    for colour_draw in colour_draws
    if
    (
        (all(x <= max_blue for x in colour_draw["blue_draws"])) &
        (all(x <= max_green for x in colour_draw["green_draws"])) &
        (all(x <= max_red for x in colour_draw["red_draws"]))
    )
]
print(sum(correct_games))

# Get the minimum number of cubes
min_num_cubes = [
    [
        max(colour_draw["blue_draws"]),
        max(colour_draw["green_draws"]),
        max(colour_draw["red_draws"])
    ]
    for colour_draw in colour_draws
]

print(sum(
    [
        np.prod(min_num_cube)
        for min_num_cube in min_num_cubes
    ]
))

