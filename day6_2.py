from collections import Counter, deque

with open("input_day6.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

marker_length = 14
indices_of_unique = []
for line in lines:
    curr_letters = deque(line[0:marker_length])
    if len(Counter(curr_letters).keys()) == marker_length:
        index_of_unique = marker_length  # zero-index of py
        break
    for idx in range(marker_length, len(line)):
        curr_letters.popleft()
        curr_letters.append(line[idx])
        if len(Counter(curr_letters).keys()) == marker_length:
            index_of_unique = idx + 1  # zero-index of py
            break
    indices_of_unique.append(index_of_unique)

print(indices_of_unique)

        