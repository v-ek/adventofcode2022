import string

with open("input_day3.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

letters = string.ascii_lowercase + string.ascii_uppercase
priorities_map = {letter: prio for letter, prio in zip(letters, range(1, len(letters) + 1 ))}

priorites = []

# Split rucksacks into chunks of 3
chunks = [lines[idx:idx+3] for idx in range(0, len(lines), 3)]
for chunk in chunks:
    uniq_1 = {item for item in chunk[0]}
    uniq_2 = {item for item in chunk[1]}
    uniq_3 = {item for item in chunk[2]}
    common_item = (uniq_1 & uniq_2 & uniq_3).pop()
    priorites.append(priorities_map[common_item])

print(priorites)
print(sum(priorites))