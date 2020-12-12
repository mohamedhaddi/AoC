with open("input", "r") as file:
    input = file.read().splitlines()

directions = ["east", "south", "west", "north"]
longitude, latitude, turn = 0, 0, 0
current_direction = directions[0]

for instruction in input:

    action, value = instruction[0], int(instruction[1:])

    if action == "F":
        if current_direction == "east":
            longitude += value
        elif current_direction == "west":
            longitude -= value
        elif current_direction == "north":
            latitude += value
        elif current_direction == "south":
            latitude -= value
    elif action == "E":
        longitude += value
    elif action == "W":
        longitude -= value
    elif action == "N":
        latitude += value
    elif action == "S":
        latitude -= value
    elif action == "R":
        turn = directions.index(current_direction) + value // 90
        if turn > 3:
            turn = turn - 4
        current_direction = directions[turn]
    elif action == "L":
        turn = directions.index(current_direction) - value // 90
        if turn < 0:
            turn = turn + 4
        current_direction = directions[turn]

print(abs(longitude) + abs(latitude))
