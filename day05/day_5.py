import re

def get_seeds(array):
    return array.lstrip("seeds:")

def map_destination_to_source(source_val):
    value = source_val
    for current_map in maps:
        value = next(
            (
                destination_range.start + (value - source_range.start)
                for source_range, destination_range in current_map.items()
                if value in source_range
            ),
            value 
        )
    return value

with open("day05/input.txt") as f:
    lines = [line.strip() for line in f]
    lines = [line for line in lines if line]


###########################################
#
# PART 1
#
###########################################
    
maps = []
for line in lines: 
    if "seeds" in line:
        seeds = get_seeds(line)
        seeds = [int(seed) for seed in seeds.split()]
    elif "map" in line: 
        maps.append(dict())
    else: 
        destination, source, length = [int(value) for value in line.split()]
        maps[-1][range(source, source+length)] = range(destination, destination+length)

locations = [map_destination_to_source(seed) for seed in seeds]
print(f"Part 1: minimum destination = {min(locations)}")

###########################################
#
# PART 2
#
###########################################

def reverse_lookup_seed(location):
    value = location
    for current_map in reversed(maps):
        value = next(
            (source_range.start + (value - destination_range.start)
             for source_range, destination_range in current_map.items()
             if value in destination_range),
            value
        )
    return value


initial_seed_data = [int(seed) for seed in re.findall(r'\d+', get_seeds(line[0]))]
seed_ranges = []
for index in range(0, len(initial_seed_data) - 1, 2):
    start, length = initial_seed_data[index:index+2]
    seed_ranges.append(range(start, start+length))

location = 0
while True:
    potential_seed = reverse_lookup_seed(location)
    if any(potential_seed in seed_range for seed_range in seed_ranges):
        print(location)
        break
    location += 1