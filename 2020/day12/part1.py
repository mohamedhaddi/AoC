with open("input", "r") as file:
    input = file.read().splitlines()

directions = ["east", "south", "west", "north"]
current_direction = directions[0]
longitude, latitude, turn = 0, 0, 0

for instruction in input:

    action, value = instruction[0], int(instruction[1:])

    if action == "R":
        turn = directions.index(current_direction) + (value // 90)
        current_direction = directions[turn if turn < 4 else turn - 4]

    elif action == "L":
        turn = directions.index(current_direction) - (value // 90)
        current_direction = directions[turn if turn >= 0 else turn + 4]

    elif action == "E" or (action == "F" and current_direction == "east"):
        longitude += value

    elif action == "W" or (action == "F" and current_direction == "west"):
        longitude -= value

    elif action == "N" or (action == "F" and current_direction == "north"):
        latitude += value

    elif action == "S" or (action == "F" and current_direction == "south"):
        latitude -= value

print(abs(longitude) + abs(latitude))
