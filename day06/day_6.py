import numpy as np

with open("day06/input.txt") as f:
    lines = [line.split() for line in f]

def get_part_1_times_and_records(lines): 
    lines[0].remove("Time:")
    race_times = [int(time) for time in lines[0]]
    lines[1].remove("Distance:")
    record_distances = [int(distance) for distance in lines[1]]
    return race_times, record_distances

def calculate_ditance_travelled(race_time): 
    return [i * (race_time - i) for i in range(race_time)]

def get_num_of_winning_ways(distances, record_distance): 
    return sum([distance > record_distance for distance in distances])

###############################################################################
#
#  PART 1
#
###############################################################################
race_times, record_distances = get_part_1_times_and_records(lines)
distances_travelled = [calculate_ditance_travelled(race_time) for race_time in race_times]
num_winning_races = [
    get_num_of_winning_ways(distances, record_distance) 
    for distances, record_distance in zip(distances_travelled, record_distances)
]
print(np.prod(num_winning_races))

###############################################################################
#
#  PART 2
#
###############################################################################
def get_part_2_time_and_record(lines): 
    part_2_race_time = "".join(lines[0])
    part_2_record_distance = "".join(lines[1])
    return int(part_2_race_time), int(part_2_record_distance)

part_2_race_time, part_2_record_distance = get_part_2_time_and_record(lines)
distances_travelled_p2 = calculate_ditance_travelled(part_2_race_time)
num_winning_races_p2 = [
    distance > part_2_record_distance 
    for distance in distances_travelled_p2
]

print(sum(num_winning_races_p2))