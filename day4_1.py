with open("input_day4.txt") as file:
    lines = file.readlines()
    lines = [line.strip().split(",") for line in lines]

num_subsets = 0

# Idea: create sets from each range and check for subsets
for line in lines:
    range1 = line[0].split("-")
    assignment1 = set(range(int(range1[0]), int(range1[1])+1))
    range2 = line[1].split("-")
    assignment2 = set(range(int(range2[0]), int(range2[1])+1))
    if assignment1.issubset(assignment2) or assignment2.issubset(assignment1):
        num_subsets += 1

print(num_subsets)