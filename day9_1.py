with open("input_day9.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

# x, y, regular right-handed coordinates
head_pos = [0, 0]
tail_pos = [0, 0]

visited_head = []
visited_tail = []

visited_head.append(tuple(head_pos))
visited_tail.append(tuple(tail_pos))

for line in lines:
    components = line.split(" ")
    direction = components[0]
    distance = int(components[1])

    for ii in range(distance):
        if direction == "R":
            head_pos[0] = head_pos[0] + 1
        elif direction == "L":
            head_pos[0] = head_pos[0] - 1
        elif direction == "U":
            head_pos[1] = head_pos[1] + 1
        elif direction == "D":
            head_pos[1] = head_pos[1] - 1
        
        d_x = head_pos[0] - tail_pos[0]
        d_y = head_pos[1] - tail_pos[1]

        if d_x >= 2:
            tail_pos[0] = tail_pos[0] + 1
            if d_y >= 1:
                tail_pos[1] = tail_pos[1] + 1
            elif d_y <= -1:
                tail_pos[1] = tail_pos[1] - 1
        elif d_x <= -2:
            tail_pos[0] = tail_pos[0] - 1
            if d_y >= 1:
                tail_pos[1] = tail_pos[1] + 1
            elif d_y <= -1:
                tail_pos[1] = tail_pos[1] - 1
        elif d_y >= 2:
            tail_pos[1] = tail_pos[1] + 1
            if d_x >= 1:
                tail_pos[0] = tail_pos[0] + 1
            elif d_x <= -1:
                tail_pos[0] = tail_pos[0] - 1
        elif d_y <= -2:
            tail_pos[1] = tail_pos[1] - 1
            if d_x >= 1:
                tail_pos[0] = tail_pos[0] + 1
            elif d_x <= -1:
                tail_pos[0] = tail_pos[0] - 1

        visited_head.append(tuple(head_pos))
        visited_tail.append(tuple(tail_pos))
            
print(visited_head)
print(visited_tail)
print(len(set(visited_head)))
print(len(set(visited_tail)))