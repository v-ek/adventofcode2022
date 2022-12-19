with open("input_day10.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

# zero-indexing, value during!
x_values = [1]

for line in lines:
    components = line.split(" ")
    instruction = components[0]

    if instruction == "noop":
        x_values.append(x_values[-1])
    elif instruction == "addx":
        value = int(components[1])
        x_values.append(x_values[-1])
        x_values.append(x_values[-1] + value)

pixels = []
for i_x in range(6):
    row = []
    for i_y in range(40):
        total_index = i_x * 40 + i_y
        sprite_pos = list(range(x_values[total_index]-1, x_values[total_index]+2))
        if i_y in sprite_pos:
            row.append("#")
        else:
            row.append(".")
    pixels.append("".join(row))

for row in pixels:
    print(row)