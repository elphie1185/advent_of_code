# PX1 + VX1*t = PX2 + VX2*t
# PX1 - PX2 = VX2*t - VX1*t
# (PX1-PX2)/(VX2-VX1) = t

def get_time(p1, p2, v1, v2): 
    return (p1 - p2)/(v2 - v1)

# read the file
with open("day24/test_input.txt") as f:
    lines = [line.strip() for line in f]

# create a list of positions and speeds
hailstones_speeds_and_position = []
for line in lines: 
    positions, speeds = line.strip().split(" @ ")
    p0_x, p0_y, p0_z = list(map(int, positions.split(", ")))
    speed_x, speed_y, speed_z = list(map(int, speeds.split(", ")))
    hailstones_speeds_and_position.append(
        (p0_x, p0_y, p0_z, speed_x, speed_y, speed_z)
    )

# for line in lines: 
#     print(line.split("@"))

