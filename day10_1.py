with open("input_day10.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

# zero-indexing, value during!
x_values = [1]

cycle_indices = [19 + idx * 40 for idx in range(6)]

for line in lines:
    components = line.split(" ")
    instruction = components[0]

    if instruction == "noop":
        x_values.append(x_values[-1])
    elif instruction == "addx":
        value = int(components[1])
        x_values.append(x_values[-1])
        x_values.append(x_values[-1] + value)

all_signal_strengths = [(idx + 1) * value for idx, value in enumerate(x_values)]

total_signal_length = sum((all_signal_strengths[idx] for idx in cycle_indices))
print(total_signal_length)