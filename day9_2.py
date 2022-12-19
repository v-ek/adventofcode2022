with open("input_day9.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

# x, y, regular right-handed coordinates
positions = [[0, 0] for idx in range(0, 10)]
visited_tail = []
visited_tail.append(tuple(positions[-1]))
n_pieces = len(positions)

for line in lines:
    components = line.split(" ")
    direction = components[0]
    distance = int(components[1])

    for ii in range(distance):
        if direction == "R":
            positions[0][0] = positions[0][0] + 1
        elif direction == "L":
            positions[0][0] = positions[0][0] - 1
        elif direction == "U":
            positions[0][1] = positions[0][1] + 1
        elif direction == "D":
            positions[0][1] = positions[0][1] - 1
        
        for piece in range(0, n_pieces-1):
            print(positions)
            
            d_x = positions[piece][0] - positions[piece+1][0]
            d_y = positions[piece][1] - positions[piece+1][1]

            if d_x >= 2:
                positions[piece+1][0] = positions[piece+1][0] + 1
                if d_y >= 1:
                    positions[piece+1][1] = positions[piece+1][1] + 1
                elif d_y <= -1:
                    positions[piece+1][1] = positions[piece+1][1] - 1
            elif d_x <= -2:
                positions[piece+1][0] = positions[piece+1][0] - 1
                if d_y >= 1:
                    positions[piece+1][1] = positions[piece+1][1] + 1
                elif d_y <= -1:
                    positions[piece+1][1] = positions[piece+1][1] - 1
            elif d_y >= 2:
                positions[piece+1][1] = positions[piece+1][1] + 1
                if d_x >= 1:
                    positions[piece+1][0] = positions[piece+1][0] + 1
                elif d_x <= -1:
                    positions[piece+1][0] = positions[piece+1][0] - 1
            elif d_y <= -2:
                positions[piece+1][1] = positions[piece+1][1] - 1
                if d_x >= 1:
                    positions[piece+1][0] = positions[piece+1][0] + 1
                elif d_x <= -1:
                    positions[piece+1][0] = positions[piece+1][0] - 1

        visited_tail.append(tuple(positions[-1]))

print(visited_tail)
print(len(set(visited_tail)))