with open("input_day2.txt") as file:
    lines = file.readlines()
matchups = [line.strip().split(" ") for line in lines]
print(matchups)

LOSS = 0
DRAW = 3
WIN = 6

points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

points_per_round = []

for play in matchups:
    opponent = play[0]
    result = play[1]
    curr_points = 0
    if result == "X":
        curr_points += LOSS
        if opponent == "A":
            curr_points += points["scissors"]
        elif opponent == "B":
            curr_points += points["rock"]
        elif opponent == "C":
            curr_points += points["paper"]
    elif result == "Y":
        curr_points += DRAW
        if opponent == "A":
            curr_points += points["rock"]
        elif opponent == "B":
            curr_points += points["paper"]
        elif opponent == "C":
            curr_points += points["scissors"]
    elif result == "Z":
        curr_points += WIN
        if opponent == "A":
            curr_points += points["paper"]
        elif opponent == "B":
            curr_points += points["scissors"]
        elif opponent == "C":
            curr_points += points["rock"]

    points_per_round.append(curr_points)

print(points_per_round)
print(sum(points_per_round))