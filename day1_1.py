with open("input_day1.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

sums = []
partial_sum = 0
for line in lines:
    try:
        partial_sum += int(line)
    except ValueError:
        sums.append(partial_sum)
        partial_sum = 0
else:  # If loop ends we are on the last entry
    sums.append(partial_sum)
print(max(sums))
print(sum(list(sorted(sums, reverse=True))[0:3]))