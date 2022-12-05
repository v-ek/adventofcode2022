from collections import deque

with open("input_day5.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

# Find the blank row, and split the lines into state and instructions
initial_state = []
instructions = []
mode = 0  # Flag for mode in parsing, 0 = initial 1 = instructions

# Split into initial state and instructions
for line in lines:
    if mode == 0 and line != "":
        # Fixed-width with 3 per col + 1 padding = 4 (except rightmost)
        initial_state.append([line[i : i + 4] for i in range(0, len(line), 4)])
    elif mode == 0 and line == "":
        mode = 1
    else:
        instructions.append(line)
state = {}
initial_state.reverse()
# Transpose the initial state with zip
for stack in zip(*initial_state):
    # Make a deque of each stack of, and store in a state dict with keys
    state[stack[0].strip()] = deque(
        [
            elem.strip().replace("]", "").replace("[", "")
            for elem in stack[1:]
            if elem.strip() != ""
        ]
    )

for line in instructions:
    instructions = line.split(" ")
    elements_to_move = int(instructions[1])
    stack_from = instructions[3]
    stack_to = instructions[5]
    for idx in range(elements_to_move):
        state[stack_to].append(state[stack_from].pop())

print("".join(stack[-1] for stack in state.values()))