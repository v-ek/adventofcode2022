with open("input_day2.txt") as file:
    lines = file.readlines()
matchups = [line.strip().split(" ") for line in lines]
print(matchups)

LOSS = 0
DRAW = 3
WIN = 6

points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

points_per_round = []

for play in matchups:
    opponent = play[0]
    you = play[1]
    curr_points = 0
    curr_points += points[you]
    if opponent == "A":
        if you == "X":
            curr_points += DRAW
        elif you == "Y":
            curr_points += WIN
        elif you == "Z":
            curr_points += LOSS
    elif opponent == "B":
        if you == "X":
            curr_points += LOSS
        elif you == "Y":
            curr_points += DRAW
        elif you == "Z":
            curr_points += WIN
    elif opponent == "C":
        if you == "X":
            curr_points += WIN
        elif you == "Y":
            curr_points += LOSS
        elif you == "Z":
            curr_points += DRAW
    points_per_round.append(curr_points)

print(points_per_round)
print(sum(points_per_round))