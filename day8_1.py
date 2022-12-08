with open("input_day8.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

len_x = len(lines[0])  # X = left-right
len_y = len(lines)  # Y = Top botton, higher = downvards

outer_visible = 2*len_x + 2*len_y - 4

# Pass 1: Build the grid of heights as an array
rows = []
cols = [] 
for line in lines:
    rows.append([int(height) for height in line])
for col in zip(*rows):
    cols.append(list(col))

visible_points = []

for y in range(1, len_y-1):
    for x in range(1, len_x-1):
        curr_col = cols[x]
        curr_row = rows[y]
        curr_height = curr_col[y]  # Or rows[x]
        if (curr_height > max(curr_col[:y])
            or curr_height > max(curr_col[y+1:])
            or curr_height > max(curr_row[:x])
            or curr_height > max(curr_row[x+1:])
        ):
            visible_points.append((x, y, curr_height))
            
print(outer_visible + len(visible_points))