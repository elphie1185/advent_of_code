import re
from itertools import cycle


def get_directions_split(direction):
    return re.findall(r"[\w']+", direction)

def get_next_location_list(current_locations, directions, step):
    return [directions[current_location][step] for current_location in current_locations]

def check_locations_end_with_Z(locations_list):
    return all(location.endswith("Z") for location in locations_list)

def get_n_steps_part_1(steps, directions, location):
    n_step = 0
    for step in cycle(steps):
        if location != "ZZZ":
            n_step += 1
            location = directions[location][step]
        else:
            break
    return n_step

def get_n_steps_part_2(steps, directions, locations):
    n_step = 0
    for step in cycle(steps):
        if not check_locations_end_with_Z(locations):
            n_step+=1
            locations = get_next_location_list(locations, directions, step)
            if n_step%5000000 == 0:
                print(n_step)
        else:
            break
    return n_step

with open("day08/input.txt") as f:
    lines = [line.strip() for line in f]
    lines = [line for line in lines if line]

steps = lines[0]
direction_mappings = [get_directions_split(direction) for direction in lines[1:]]

directions = {
    direction_mapping[0]: {
            "L":direction_mapping[1],
            "R": direction_mapping[2],
    }
    for direction_mapping in direction_mappings
}

###############################################################################
#
#  PART 1
#
###############################################################################
location = "AAA"
n_steps = get_n_steps_part_1(steps, directions, location)
print(n_steps)

###############################################################################
#
#  PART 2
#
###############################################################################

start_locations = [location for location in list(directions.keys()) if location.endswith("A")]
n_steps = get_n_steps_part_2(steps, directions, start_locations)

print(len(n_steps))