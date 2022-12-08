def get_viewing_distance(height, trees):
    distance = 0
    for curr_height in trees:
        distance +=1
        if curr_height >= height:
            return distance
    return distance

with open("input_day8.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

len_x = len(lines[0])  # X = left-right
len_y = len(lines)  # Y = Top botton, higher = downvards

# Pass 1: Build the grid of heights as an array
rows = []
cols = [] 
for line in lines:
    rows.append([int(height) for height in line])
for col in zip(*rows):
    cols.append(list(col))

points_with_scores = []
scenic_scores = []

for y in range(1, len_y-1):
    for x in range(1, len_x-1):
        curr_col = cols[x]
        curr_row = rows[y]
        curr_height = curr_col[y]  # Or rows[x]

        d_u = get_viewing_distance(curr_height, reversed(curr_col[:y]))
        d_d = get_viewing_distance(curr_height, curr_col[y+1:])
        d_l = get_viewing_distance(curr_height, reversed(curr_row[:x]))
        d_r = get_viewing_distance(curr_height, curr_row[x+1:])
        scenic_score = d_u * d_d * d_l * d_r
        
        points_with_scores.append((x, y, scenic_score))
        scenic_scores.append(scenic_score)

print(points_with_scores)
print(max(scenic_scores))
