with open("input", "r") as file:
    input = file.read().splitlines()

ship = {"longitude": 0, "latitude": 0}
waypoint = {
    "longitude": 10,
    "latitude": 1,
    "relative_longitude": 10,
    "relative_latitude": 1,
}

for instruction in input:

    action, value = instruction[0], int(instruction[1:])

    if action == "F":
        ship["longitude"] += waypoint["relative_longitude"] * value
        ship["latitude"] += waypoint["relative_latitude"] * value
        waypoint["longitude"] = ship["longitude"] + waypoint["relative_longitude"]
        waypoint["latitude"] = ship["latitude"] + waypoint["relative_latitude"]

    elif action == "N":
        waypoint["relative_latitude"] += value
        waypoint["latitude"] += waypoint["relative_latitude"]

    elif action == "S":
        waypoint["relative_latitude"] -= value
        waypoint["latitude"] -= abs(waypoint["relative_latitude"])

    elif action == "E":
        waypoint["relative_longitude"] += value
        waypoint["longitude"] += waypoint["relative_longitude"]

    elif action == "W":
        waypoint["relative_longitude"] -= value
        waypoint["longitude"] -= abs(waypoint["relative_longitude"])

    elif (action == "R" and value == 90) or (action == "L" and value == 270):
        waypoint["relative_longitude"], waypoint["relative_latitude"] = (
            waypoint["relative_latitude"],
            -1 * waypoint["relative_longitude"],
        )
        waypoint["longitude"], waypoint["latitude"] = (
            waypoint["latitude"],
            -1 * waypoint["longitude"],
        )

    elif action in "LR" and value == 180:
        waypoint["relative_longitude"], waypoint["relative_latitude"] = (
            -1 * waypoint["relative_longitude"],
            -1 * waypoint["relative_latitude"],
        )
        waypoint["longitude"], waypoint["latitude"] = (
            -1 * waypoint["longitude"],
            -1 * waypoint["latitude"],
        )

    elif (action == "R" and value == 270) or (action == "L" and value == 90):
        waypoint["relative_longitude"], waypoint["relative_latitude"] = (
            -1 * waypoint["relative_latitude"],
            waypoint["relative_longitude"],
        )
        waypoint["longitude"], waypoint["latitude"] = (
            -1 * waypoint["latitude"],
            waypoint["longitude"],
        )

print(abs(ship["longitude"]) + abs(ship["latitude"]))
