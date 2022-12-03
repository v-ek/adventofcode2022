import string

with open("input_day3.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

letters = string.ascii_lowercase + string.ascii_uppercase
priorities_map = {letter: prio for letter, prio in zip(letters, range(1, len(letters) + 1 ))}

priorites = []

for line in lines:
    length = len(line)
    comp1, comp2 = line[0:length/2], line[length/2:length]
    uniq_comp1 = {item for item in comp1}
    uniq_comp2 = {item for item in comp2}
    common_item = (uniq_comp1 & uniq_comp2).pop()
    priorites.append(priorities_map[common_item])

print(priorites)
print(sum(priorites))